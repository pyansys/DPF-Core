from ansys.dpf.core.mapping_types import map_types_to_cpp, map_types_to_python


class Output:
    def __init__(self, spec, pin, operator):
        self._spec = spec
        self._operator = operator
        self._pin = pin
        self._python_expected_types = []
        for cpp_type in self._spec.type_names:
            self._python_expected_types.append(map_types_to_python[cpp_type])

    def get_data(self):
        """Returns this output of this operator"""
        type_output = self._spec.type_names[0]
        if type_output == 'abstract_meshed_region':
            type_output= 'meshed_region'
            
        elif  type_output == "fields_container":
            type_output = ['collection','field']

        return self._operator.get_output(self._pin, type_output)

    def __call__(self):
        return self.get_data()
    
    def __str__(self): 
        docstr ='\033[1m'+ self._spec.name+'\033[0m' 
        if self._spec.optional :
            docstr+=" (optional)"
        docstr+=", expects types:"+'\n'
        for types in  self._python_expected_types:
            docstr+="   -"+types +'\n'
        if self._spec.document :
            docstr+="help: "+self._spec.document +'\n'
        return docstr


class _Outputs:
    def __init__(self, dict_outputs, operator):
        self._dict_outputs = dict_outputs
        self._operator = operator
        self._outputs = []
        for pin in self._dict_outputs:
            if len(self._dict_outputs[pin].type_names) and self._dict_outputs[pin] is not None:
                output_name = self._dict_outputs[pin].name
                self._outputs.append(output_name)
                output = Output(self._dict_outputs[pin], pin, self._operator)
                # setattr(self, output_name, output)

    def _get_given_output(self, input_type_name):
        corresponding_pins = []
        for asked_camel_types in input_type_name:
            for pin in self._dict_outputs:
                for cpp_type in self._dict_outputs[pin].type_names:
                    if map_types_to_python[cpp_type] == asked_camel_types:
                        corresponding_pins.append(pin) 
                    elif asked_camel_types =="Any":
                        corresponding_pins.append(pin)
        return corresponding_pins

    def __str__(self):
        docstr = 'Available outputs:\n'
        for output in self._outputs :
            tot_string =output.__str__()
            input_string = tot_string.split('\n')
            input_string1 = input_string[0]
            line = ["   ","o ",input_string1]
            docstr+='{:<5}{:<4}{:<20}'.format(*line)
            docstr+='\n'
            for inputstr in input_string :
                if inputstr != input_string1:
                    line = ["   ","  ",inputstr]
                    docstr+='{:<5}{:<4}{:<20}'.format(*line)
                    docstr+='\n'
        return docstr

#Dynamic class Outputs
class Outputs(_Outputs):
    def __init__(self, dict_outputs, operator):
        self._dict_outputs = dict_outputs
        self._operator = operator
        self._outputs = []
        for pin in self._dict_outputs:
            if len(self._dict_outputs[pin].type_names) and self._dict_outputs[pin] is not None:
                output_name = self._dict_outputs[pin].name
                self._outputs.append(output_name)
                output = Output(self._dict_outputs[pin], pin, self._operator)
                setattr(self, output_name, output)