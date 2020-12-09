from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.Native.dll plugin, from "utility" category
"""

#internal name: ExtractFromFC
#scripting name: extract_field
def _get_input_spec_extract_field(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["field","fields_container"], optional = False, document = """if a field is in input, it is passed on as output""")
    inputs_dict_extract_field = { 
        0 : inpin0
    }
    return inputs_dict_extract_field[pin]

def _get_output_spec_extract_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_extract_field = { 
        0 : outpin0
    }
    return outputs_dict_extract_field[pin]

class _InputSpecExtractField(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_extract_field(0), 0, op, -1) 

class _OutputSpecExtractField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_extract_field(0), 0, op) 

class _ExtractField:
    """Operator's description:
Internal name is "ExtractFromFC"
Scripting name is "extract_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("ExtractFromFC")
- using dpf.operators.utility.extract_field()

Input list: 
   0: fields_container (if a field is in input, it is passed on as output)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "ExtractFromFC"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecExtractField(self._op)
         self.outputs = _OutputSpecExtractField(self._op)

def extract_field():
    return _ExtractField()

#internal name: BindSupport
#scripting name: bind_support
def _get_input_spec_bind_support(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "support", type_names = ["meshed_region","abstract_field_support"], optional = False, document = """meshed region or a support of the field""")
    inputs_dict_bind_support = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_bind_support[pin]

def _get_output_spec_bind_support(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_bind_support = { 
        0 : outpin0
    }
    return outputs_dict_bind_support[pin]

class _InputSpecBindSupport(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_bind_support(0), 0, op, -1) 
        self.support = _Input(_get_input_spec_bind_support(1), 1, op, -1) 

class _OutputSpecBindSupport(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_bind_support(0), 0, op) 

class _BindSupport:
    """Operator's description:
Internal name is "BindSupport"
Scripting name is "bind_support"

This operator can be instantiated in both following ways:
- using dpf.Operator("BindSupport")
- using dpf.operators.utility.bind_support()

Input list: 
   0: field (field or fields container with only one field is expected)
   1: support (meshed region or a support of the field)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "BindSupport"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecBindSupport(self._op)
         self.outputs = _OutputSpecBindSupport(self._op)

def bind_support():
    return _BindSupport()

#internal name: change_location
#scripting name: change_location
def _get_input_spec_change_location(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "new_location", type_names = ["string"], optional = False, document = """new location of the output field ex: 'Nodal', 'ElementalNodal', 'Elemental'...""")
    inputs_dict_change_location = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_change_location[pin]

def _get_output_spec_change_location(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_change_location = { 
        0 : outpin0
    }
    return outputs_dict_change_location[pin]

class _InputSpecChangeLocation(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_change_location(0), 0, op, -1) 
        self.new_location = _Input(_get_input_spec_change_location(1), 1, op, -1) 

class _OutputSpecChangeLocation(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_change_location(0), 0, op) 

class _ChangeLocation:
    """Operator's description:
Internal name is "change_location"
Scripting name is "change_location"

This operator can be instantiated in both following ways:
- using dpf.Operator("change_location")
- using dpf.operators.utility.change_location()

Input list: 
   0: field 
   1: new_location (new location of the output field ex: 'Nodal', 'ElementalNodal', 'Elemental'...)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "change_location"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecChangeLocation(self._op)
         self.outputs = _OutputSpecChangeLocation(self._op)

def change_location():
    return _ChangeLocation()

#internal name: InjectToFieldContainer
#scripting name: field_to_fc
def _get_input_spec_field_to_fc(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """if a fields container is set in input, it is pass on as output.""")
    inputs_dict_field_to_fc = { 
        0 : inpin0
    }
    return inputs_dict_field_to_fc[pin]

def _get_output_spec_field_to_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_field_to_fc = { 
        0 : outpin0
    }
    return outputs_dict_field_to_fc[pin]

class _InputSpecFieldToFc(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_field_to_fc(0), 0, op, -1) 

class _OutputSpecFieldToFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_field_to_fc(0), 0, op) 

class _FieldToFc:
    """Operator's description:
Internal name is "InjectToFieldContainer"
Scripting name is "field_to_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("InjectToFieldContainer")
- using dpf.operators.utility.field_to_fc()

Input list: 
   0: field (if a fields container is set in input, it is pass on as output.)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "InjectToFieldContainer"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecFieldToFc(self._op)
         self.outputs = _OutputSpecFieldToFc(self._op)

def field_to_fc():
    return _FieldToFc()

#internal name: strain_from_voigt
#scripting name: strain_from_voigt
def _get_input_spec_strain_from_voigt(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_strain_from_voigt = { 
        0 : inpin0
    }
    return inputs_dict_strain_from_voigt[pin]

def _get_output_spec_strain_from_voigt(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_strain_from_voigt = { 
        0 : outpin0
    }
    return outputs_dict_strain_from_voigt[pin]

class _InputSpecStrainFromVoigt(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_strain_from_voigt(0), 0, op, -1) 

class _OutputSpecStrainFromVoigt(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_strain_from_voigt(0), 0, op) 

class _StrainFromVoigt:
    """Operator's description:
Internal name is "strain_from_voigt"
Scripting name is "strain_from_voigt"

This operator can be instantiated in both following ways:
- using dpf.Operator("strain_from_voigt")
- using dpf.operators.utility.strain_from_voigt()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "strain_from_voigt"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecStrainFromVoigt(self._op)
         self.outputs = _OutputSpecStrainFromVoigt(self._op)

def strain_from_voigt():
    return _StrainFromVoigt()

#internal name: field::set_property
#scripting name: set_property
def _get_input_spec_set_property(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "property_name", type_names = ["string"], optional = False, document = """Property to set""")
    inpin2 = _PinSpecification(name = "property_value", type_names = ["string","int32","double"], optional = False, document = """Property to set""")
    inputs_dict_set_property = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    return inputs_dict_set_property[pin]

def _get_output_spec_set_property(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], document = """""")
    outputs_dict_set_property = { 
        0 : outpin0
    }
    return outputs_dict_set_property[pin]

class _InputSpecSetProperty(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_set_property(0), 0, op, -1) 
        self.property_name = _Input(_get_input_spec_set_property(1), 1, op, -1) 
        self.property_value = _Input(_get_input_spec_set_property(2), 2, op, -1) 

class _OutputSpecSetProperty(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_set_property(0), 0, op) 

class _SetProperty:
    """Operator's description:
Internal name is "field::set_property"
Scripting name is "set_property"

This operator can be instantiated in both following ways:
- using dpf.Operator("field::set_property")
- using dpf.operators.utility.set_property()

Input list: 
   0: field 
   1: property_name (Property to set)
   2: property_value (Property to set)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "field::set_property"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecSetProperty(self._op)
         self.outputs = _OutputSpecSetProperty(self._op)

def set_property():
    return _SetProperty()

#internal name: fieldify
#scripting name: scalars_to_field
def _get_input_spec_scalars_to_field(pin):
    inpin0 = _PinSpecification(name = "double_or_vector_double", type_names = ["double"], optional = False, document = """double or vector of double""")
    inputs_dict_scalars_to_field = { 
        0 : inpin0
    }
    return inputs_dict_scalars_to_field[pin]

def _get_output_spec_scalars_to_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_scalars_to_field = { 
        0 : outpin0
    }
    return outputs_dict_scalars_to_field[pin]

class _InputSpecScalarsToField(_Inputs):
    def __init__(self, op: _Operator):
        self.double_or_vector_double = _Input(_get_input_spec_scalars_to_field(0), 0, op, -1) 

class _OutputSpecScalarsToField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_scalars_to_field(0), 0, op) 

class _ScalarsToField:
    """Operator's description:
Internal name is "fieldify"
Scripting name is "scalars_to_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("fieldify")
- using dpf.operators.utility.scalars_to_field()

Input list: 
   0: double_or_vector_double (double or vector of double)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "fieldify"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecScalarsToField(self._op)
         self.outputs = _OutputSpecScalarsToField(self._op)

def scalars_to_field():
    return _ScalarsToField()

#internal name: html_doc
#scripting name: html_doc
def _get_input_spec_html_doc(pin):
    inpin0 = _PinSpecification(name = "output_path", type_names = ["string"], optional = True, document = """default is {working directory}/dataProcessingDoc.html""")
    inputs_dict_html_doc = { 
        0 : inpin0
    }
    return inputs_dict_html_doc[pin]

def _get_output_spec_html_doc(pin):
    outputs_dict_html_doc = {
    }
    return outputs_dict_html_doc[pin]

class _InputSpecHtmlDoc(_Inputs):
    def __init__(self, op: _Operator):
        self.output_path = _Input(_get_input_spec_html_doc(0), 0, op, -1) 

class _OutputSpecHtmlDoc(_Outputs):
    def __init__(self, op: _Operator):
        pass 

class _HtmlDoc:
    """Operator's description:
Internal name is "html_doc"
Scripting name is "html_doc"

This operator can be instantiated in both following ways:
- using dpf.Operator("html_doc")
- using dpf.operators.utility.html_doc()

Input list: 
   0: output_path (default is {working directory}/dataProcessingDoc.html)
Output list: 
   empty 
"""
    def __init__(self):
         self._name = "html_doc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecHtmlDoc(self._op)
         self.outputs = _OutputSpecHtmlDoc(self._op)

def html_doc():
    return _HtmlDoc()

#internal name: make_unit
#scripting name: unitary_field
def _get_input_spec_unitary_field(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_unitary_field = { 
        0 : inpin0
    }
    return inputs_dict_unitary_field[pin]

def _get_output_spec_unitary_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_unitary_field = { 
        0 : outpin0
    }
    return outputs_dict_unitary_field[pin]

class _InputSpecUnitaryField(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_unitary_field(0), 0, op, -1) 

class _OutputSpecUnitaryField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_unitary_field(0), 0, op) 

class _UnitaryField:
    """Operator's description:
Internal name is "make_unit"
Scripting name is "unitary_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("make_unit")
- using dpf.operators.utility.unitary_field()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "make_unit"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecUnitaryField(self._op)
         self.outputs = _OutputSpecUnitaryField(self._op)

def unitary_field():
    return _UnitaryField()

#internal name: forward
#scripting name: forward_field
def _get_input_spec_forward_field(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_forward_field = { 
        0 : inpin0
    }
    return inputs_dict_forward_field[pin]

def _get_output_spec_forward_field(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_forward_field = { 
        0 : outpin0
    }
    return outputs_dict_forward_field[pin]

class _InputSpecForwardField(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_forward_field(0), 0, op, -1) 

class _OutputSpecForwardField(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_forward_field(0), 0, op) 

class _ForwardField:
    """Operator's description:
Internal name is "forward"
Scripting name is "forward_field"

This operator can be instantiated in both following ways:
- using dpf.Operator("forward")
- using dpf.operators.utility.forward_field()

Input list: 
   0: field (field or fields container with only one field is expected)
Output list: 
   0: field 
"""
    def __init__(self):
         self._name = "forward"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecForwardField(self._op)
         self.outputs = _OutputSpecForwardField(self._op)

def forward_field():
    return _ForwardField()

#internal name: forward_fc
#scripting name: forward_fields_container
def _get_input_spec_forward_fields_container(pin):
    inpin0 = _PinSpecification(name = "fields", type_names = ["fields_container","field"], optional = False, document = """""")
    inputs_dict_forward_fields_container = { 
        0 : inpin0
    }
    return inputs_dict_forward_fields_container[pin]

def _get_output_spec_forward_fields_container(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_forward_fields_container = { 
        0 : outpin0
    }
    return outputs_dict_forward_fields_container[pin]

class _InputSpecForwardFieldsContainer(_Inputs):
    def __init__(self, op: _Operator):
        self.fields = _Input(_get_input_spec_forward_fields_container(0), 0, op, -1) 

class _OutputSpecForwardFieldsContainer(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_forward_fields_container(0), 0, op) 

class _ForwardFieldsContainer:
    """Operator's description:
Internal name is "forward_fc"
Scripting name is "forward_fields_container"

This operator can be instantiated in both following ways:
- using dpf.Operator("forward_fc")
- using dpf.operators.utility.forward_fields_container()

Input list: 
   0: fields 
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "forward_fc"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecForwardFieldsContainer(self._op)
         self.outputs = _OutputSpecForwardFieldsContainer(self._op)

def forward_fields_container():
    return _ForwardFieldsContainer()

#internal name: text_parser
#scripting name: txt_file_to_dpf
def _get_input_spec_txt_file_to_dpf(pin):
    inpin0 = _PinSpecification(name = "input_string", type_names = ["string"], optional = False, document = """ex: "double:1.0", "int:1", "vector<double>:1.0;1.0".""")
    inputs_dict_txt_file_to_dpf = { 
        0 : inpin0
    }
    return inputs_dict_txt_file_to_dpf[pin]

def _get_output_spec_txt_file_to_dpf(pin):
    outputs_dict_txt_file_to_dpf = {
    }
    return outputs_dict_txt_file_to_dpf[pin]

class _InputSpecTxtFileToDpf(_Inputs):
    def __init__(self, op: _Operator):
        self.input_string = _Input(_get_input_spec_txt_file_to_dpf(0), 0, op, -1) 

class _OutputSpecTxtFileToDpf(_Outputs):
    def __init__(self, op: _Operator):
        pass 
        pass 

class _TxtFileToDpf:
    """Operator's description:
Internal name is "text_parser"
Scripting name is "txt_file_to_dpf"

This operator can be instantiated in both following ways:
- using dpf.Operator("text_parser")
- using dpf.operators.utility.txt_file_to_dpf()

Input list: 
   0: input_string (ex: "double:1.0", "int:1", "vector<double>:1.0;1.0".)
Output list: 
   empty 
   empty 
"""
    def __init__(self):
         self._name = "text_parser"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecTxtFileToDpf(self._op)
         self.outputs = _OutputSpecTxtFileToDpf(self._op)

def txt_file_to_dpf():
    return _TxtFileToDpf()

#internal name: BindSupportFC
#scripting name: bind_support_fc
def _get_input_spec_bind_support_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "support", type_names = ["meshed_region","abstract_field_support"], optional = False, document = """meshed region or a support of the field""")
    inputs_dict_bind_support_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_bind_support_fc[pin]

def _get_output_spec_bind_support_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_bind_support_fc = { 
        0 : outpin0
    }
    return outputs_dict_bind_support_fc[pin]

class _InputSpecBindSupportFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_bind_support_fc(0), 0, op, -1) 
        self.support = _Input(_get_input_spec_bind_support_fc(1), 1, op, -1) 

class _OutputSpecBindSupportFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_bind_support_fc(0), 0, op) 

class _BindSupportFc:
    """Operator's description:
Internal name is "BindSupportFC"
Scripting name is "bind_support_fc"

This operator can be instantiated in both following ways:
- using dpf.Operator("BindSupportFC")
- using dpf.operators.utility.bind_support_fc()

Input list: 
   0: fields_container 
   1: support (meshed region or a support of the field)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "BindSupportFC"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecBindSupportFc(self._op)
         self.outputs = _OutputSpecBindSupportFc(self._op)

def bind_support_fc():
    return _BindSupportFc()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "utility" category
"""

#internal name: change_shellLayers
#scripting name: change_shell_layers
def _get_input_spec_change_shell_layers(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "e_shell_layer", type_names = ["int32"], optional = False, document = """0:Top, 1: Bottom, 2: BottomTop, 3:Mid, 4:BottomTopMid""")
    inputs_dict_change_shell_layers = { 
        0 : inpin0,
        1 : inpin1
    }
    return inputs_dict_change_shell_layers[pin]

def _get_output_spec_change_shell_layers(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_change_shell_layers = { 
        0 : outpin0
    }
    return outputs_dict_change_shell_layers[pin]

class _InputSpecChangeShellLayers(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_change_shell_layers(0), 0, op, -1) 
        self.e_shell_layer = _Input(_get_input_spec_change_shell_layers(1), 1, op, -1) 

class _OutputSpecChangeShellLayers(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_change_shell_layers(0), 0, op) 

class _ChangeShellLayers:
    """Operator's description:
Internal name is "change_shellLayers"
Scripting name is "change_shell_layers"

This operator can be instantiated in both following ways:
- using dpf.Operator("change_shellLayers")
- using dpf.operators.utility.change_shell_layers()

Input list: 
   0: fields_container 
   1: e_shell_layer (0:Top, 1: Bottom, 2: BottomTop, 3:Mid, 4:BottomTopMid)
Output list: 
   0: fields_container 
"""
    def __init__(self):
         self._name = "change_shellLayers"
         self._op = _Operator(self._name)
         self.inputs = _InputSpecChangeShellLayers(self._op)
         self.outputs = _OutputSpecChangeShellLayers(self._op)

def change_shell_layers():
    return _ChangeShellLayers()

