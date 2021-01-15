"""Autogenerated DPF operator classes.

Created on 01/15/2021, 00:24:02
"""
from collections import OrderedDict
from collections import namedtuple
from ansys.dpf import core as dpf

InputSpec = namedtuple('InputSpec', ['document', 'ellipsis', 'name', 'optional',
                                     'type_names'])

OutputSpec = namedtuple('OutputSpec', ['name', 'type_names', 'document'])


class WrapInTopology(dpf.Operator):
    """DPF "topology::topology_from_mesh" Operator

    Take various input, and wrap in geometry if necessary.

    Available inputs:
     -   ``mesh`` : MeshedRegion, AbstractTopologyEntity

     -   ``id`` : int, optional
         Id that must be attributed to the generated geometry (default is 0).


    Available outputs:
     -   mesh


    Parameters
    ----------
    mesh : MeshedRegion or abstract_topology_entity


    id : int, optional
        Id that must be attributed to the generated geometry (default
        is 0).

    Examples
    --------
    >>> op = dpf.operators.WrapInTopology()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> op.inputs.id.connect(my_id)  # optional
    >>> my_mesh = op.outputs.mesh()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(0, InputSpec(document='', ellipsis=False, name='mesh', optional=False, type_names=['abstract_meshed_region', 'abstract_topology_entity'])), (1, InputSpec(document='Id that must be attributed to the generated geometry (default is 0).', ellipsis=False, name='id', optional=True, type_names=['int32']))])
        def __init__(self, oper):
            self._mesh = None
            self._id = None
            super().__init__(self._spec, oper)

        @property
        def mesh(self):
            return self._mesh

        @mesh.setter
        def mesh(self, mesh):
            self._mesh.connect(mesh)

        @property
        def id(self):
            """Id that must be attributed to the generated geometry (default is 0)."""
            return self._id

        @id.setter
        def id(self, id):
            self._id.connect(id)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='mesh', type_names=['abstract_topology_entity'], document=''))])
        def __init__(self, oper):
            self._mesh = None
            super().__init__(self._spec, oper)

        @property
        def mesh(self):
            """"""
            return self._mesh


    def __init__(self, mesh, id=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "topology::topology_from_mesh"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def mesh(self):
        """"""
        return self.outputs._mesh



