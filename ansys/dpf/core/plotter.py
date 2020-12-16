"""Dpf plotter class is contained in this module. 
Allows to plot a mesh and a fields container 
using pyvista."""

import pyvista as pv
import matplotlib.pyplot as pyplot
import os
import sys
from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core.rescoper import Rescoper as _Rescoper
from ansys.dpf.core.common import locations, ShellLayers

class Plotter:
    def __init__(self, mesh):
        self._mesh = mesh
        
    def plot_mesh(self, notebook=None):
        """Plot the mesh using pyvista.
        
        Parameters
        ----------
        notebook : bool, optional
            When ``None`` (default) plot a static image within an
            iPython notebook if available.  When ``False``, plot
            external to the notebook with an interactive window.  When
            ``True``, always plot within a notebook.

        """
        return self._mesh.grid.plot(notebook=notebook)
        
    def plot_chart(self, fields_container):
        """Plot the minimum/maximum result values over time 
        if the time_freq_support contains several time_steps 
        (for example: transient analysis)
        
        Parameters
        ----------
        field_container
            dpf.core.FieldsContainer that must contains a result for each time step of the time_freq_support.
        """
        tfq = fields_container.time_freq_support
        time_field = tfq.frequencies
        normOp = dpf.core.Operator("norm_fc")
        minmaxOp = dpf.core.Operator("min_max_fc")
        normOp.inputs.fields_container.connect(fields_container)
        minmaxOp.inputs.connect(normOp.outputs)
        fieldMin = minmaxOp.outputs.field_min()
        fieldMax = minmaxOp.outputs.field_max()
        pyplot.plot(time_field.data,fieldMax.data,'r',label='Maximum')
        pyplot.plot(time_field.data,fieldMin.data,'b',label='Minimum')
        pyplot.xlabel("time (s)")
        substr = fields_container[0].name.split("_")
        pyplot.ylabel(substr[0] + fieldMin.unit)
        pyplot.title( substr[0] + ": min/max values over time")
        return pyplot.legend()

    def plot_contour(self, field_or_fields_container, notebook=None):
        """Plot the contour result on its mesh support. The obtained
        figure depends on the support (can be a meshed_region or a
        time_freq_support).  If transient analysis, plot the last
        result if no time_scoping has been specified.

        Parameters
        ----------
        fields_container : dpf.core.FieldsContainer
            Field container that contains the result to plot.

        notebook : bool, optional
            When ``None`` (default) plot a static image within an
            iPython notebook if available.  When ``False``, plot
            external to the notebook with an interactive window.  When
            ``True``, always plot within a notebook.
        """
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
            
        if isinstance(field_or_fields_container, dpf.core.Field) or isinstance(field_or_fields_container, dpf.core.FieldsContainer):
            fields_container = None
            if isinstance(field_or_fields_container, dpf.core.Field):
                fields_container = dpf.core.FieldsContainer()
                fields_container.add_label('time')
                fields_container.add_field({'time':1}, field_or_fields_container)
            elif isinstance(field_or_fields_container, dpf.core.FieldsContainer):
                fields_container = field_or_fields_container
        else:
            raise Exception("Field or Fields Container only can be plotted.")
        
        plotter = pv.Plotter(notebook=notebook)
        mesh = self._mesh
        grid = mesh.grid
        nan_color = "grey"
        
        #get mesh scoping
        mesh_scoping = None
        if (fields_container[0].location == locations.nodal):
            mesh_scoping = mesh.nodes.scoping
        elif(fields_container[0].location == locations.elemental):
            mesh_scoping = mesh.elements.scoping
        else:
            raise Exception("Only elemental or nodal location are supported for plotting.")
        
        #rescoper operator from dpf with nan values as default values
        rescoperOp = dpf.core.Operator("Rescope")
        rescoperOp.inputs.mesh_scoping.connect(mesh_scoping)
        rescoperOp.inputs.fields_container.connect(fields_container)
        rescoperOp.connect(2,float("nan"))
        fields = rescoperOp.outputs.fields_container()
                
        #add meshes
        i = 0
        shelllayers_changed_fc = None
        for field in fields:
            name = field.name.split("_")[0]
            data = field.data
            #check if shell layers, if yes, make the transformation and store it
            shell_layers = field.shell_layers
            if (shell_layers == ShellLayers.TOP 
                or shell_layers == ShellLayers.MID 
                or shell_layers == ShellLayers.BOTTOM
                or shell_layers == ShellLayers.TOPBOTTOM 
                or shell_layers == ShellLayers.TOPBOTTOMMID):
                if (shelllayers_changed_fc is None):
                    changeOp = core.Operator("change_shellLayers")
                    changeOp.inputs.fields_container.connect(fields_container)
                    changeOp.inputs.e_shell_layer.connect(3) #mid layers taken
                    rescoperOp.inputs.fields_container.connect(changeOp.outputs.fields_container)
                    shelllayers_changed_fc = rescoperOp.outputs.fields_container()
                    field = shelllayers_changed_fc[i]
                    data = field.data
                else:
                    data = shelllayers_changed_fc[i].data
            plotter.add_mesh(grid, scalars = data, stitle = name, nan_color=nan_color, show_edges=True)
            i += 1
        #show result
        plotter.add_axes()
        return plotter.show()
    
    def _plot_contour_using_vtk_file(self, fields_container, notebook=None):
        """Plot the contour result on its mesh support. The obtained figure depends on the 
        support (can be a meshed_region or a time_freq_support).
        If transient analysis, plot the last result.
        
        This method is private, publishes a vtk file and print (using pyvista) from this file."""
        plotter = pv.Plotter(notebook=notebook)
        # mesh_provider = Operator("MeshProvider")
        # mesh_provider.inputs.data_sources.connect(self._evaluator._model.metadata.data_sources)
        vtk_export = dpf.core.Operator("vtk_export")
        path = os.getcwd()
        file_name = "dpf_temporary_hokflb2j9sjd0a3.vtk"
        path += "/" + file_name
        vtk_export.inputs.mesh.connect(self._mesh)
        vtk_export.inputs.fields1.connect(fields_container)
        vtk_export.inputs.file_path.connect(path)
        vtk_export.run()
        grid = pv.read(path)
        if os.path.exists(path):
            os.remove(path)
        names = grid.array_names
        field_name = fields_container[0].name
        for n in names: #get new name (for example if time_steps)
            if field_name in n:
                field_name = n #default: will plot the last time_step 
        val = grid.get_array(field_name)
        plotter.add_mesh(grid, scalars=val, stitle = field_name, show_edges=True)
        plotter.add_axes()
        plotter.show()
