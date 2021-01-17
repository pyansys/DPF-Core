"""
.. _ref_basic_harmonic:

Multi-Harmonic Response Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to to compute a multi-harmonic response 
using fft transforms

"""
import numpy as np
import matplotlib.pyplot as pyplot

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Begin by downloading the example harmonic result.  This result is
# not included in the core module by default to speed up the install.
# Download should only take a few seconds.
#
# Next, create the model and display the state of the result.  Note
# that this harmonic result file contains several rpms,
# each rpm has several frequencies.

harmonic = r'c:\temp\file_harmonic_5rpm.rst'
model = dpf.Model(harmonic)
print(model)


###############################################################################
# Read the analysis domain support 
tf = model.metadata.time_freq_support
#print(model.metadata.time_freq_support)

###############################################################################
# Load the dpf.math plugin to have access to fft operators
base = dpf.BaseService()
base.load_library("Ans.Dpf.Math.dll","math")
#you can regenerate the documentation to get the description of math operators
#doc = dpf.Operator("html_doc")
#doc.inputs.output_path.connect(r'C:\temp\dpf.html')
#doc.run()

###############################################################################
# Compute multi harmonic response
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this example we compute the response based on Rz of the selected nodes
# and through multiple rpms (multiple engine orders)

# Create a total displacement operator and set its time scoping to
# the entire time freq support and its nodes scoping into user defined nodes.
dispOp = model.operator("UTOT")
timeIds = list(range(1,model.metadata.time_freq_support.n_sets+1))

#define nodal scoping
nodes = dpf.Scoping()
nodes.ids = [2,18]

#connect the frequencies and the nodes scopings to the result provider operator
dispOp.inputs.mesh_scoping.connect(nodes)
dispOp.inputs.time_scoping.connect(timeIds)

# extract Rz component using the component selector operator
comp = dpf.Operator("component_selector_fc")
comp.inputs.connect(dispOp.outputs)
comp.inputs.component_number.connect(5)

#compute the multi-harmonic response based on Rz and a set of rpms
rpms = dpf.Scoping()
rpms.ids = [1,2,3]

fft = dpf.Operator("fft_multi_harmonic_minmax")

fft.inputs.connect(comp.outputs)
fft.inputs.rpm_scoping.connect(rpms)


fields = fft.outputs.field_max()
len(fields) #we will have a multi-harmonic response per node, here 2 fields

field1 = fields[0]
field2 = fields[1]

###############################################################################
# Plot the minimum and maximum displacements over time

pyplot.plot(field1.data,'r',label='field 1')
pyplot.plot(field2.data,'b',label="field 2")
pyplot.xlabel("freqs (Hz)")
pyplot.ylabel("displacement (m)")
pyplot.legend()
pyplot.show()