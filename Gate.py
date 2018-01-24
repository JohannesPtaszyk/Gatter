class Gate:
    def __init__(self, input_count):
        self._typ = ""
        self._input_count = input_count
        self._output = False
        self._inputs = []

        # Fill inputs array with value "true" for the given number of inputs
           
        for i in range(0, input_count):
            self._inputs.append(False)

    # Get Gate type

    def get_typ(self):
        return self._typ

    # Get number of Gate inputs

    def get_input_count(self):
        return self._input_count

    # Get array of input states

    def get_inputs(self):
        return self._inputs

    # Get state of a specific input

    def get_input_state(self, index):
        return self._inputs[index]

    # Get state of output

    def get_output_state(self):
        return self._output

    # Set state of a specific input

    def set_input_state(self, index, value):
        try:
            self._inputs[index] = value
        except():
            print("Error while setting input value")

    # Set state of output

    def set_output_state(self, value):
        self._output = value

    # Sets the output state according to the result of calc_output_state

    def refresh_output_state(self):
        self.set_output_state(self._calc_output_state())

    # Placeholder for a method to calculate and change the output depending on the inputs
    # this method has to be overwritten in the subclass

    def _calc_output_state(self):
        return "Error: " \
               "Its not possible to get an output of the 'Gate' class, please use a subclass and override this method"



# A Subclass of Gate defining an OR Gate


class OR(Gate):
    def __init__(self, input_count):
        super().__init__(input_count)
        self._typ = "COR"

    # Calc and returns output state depending on input state

    def _calc_output_state(self):
        for i in self.get_inputs():
            if self.get_input_state(i) is True:
                return True
        return False


class AND(Gate):
    def __init__(self, input_count):
        super().__init__(input_count)
        self._typ = "COR"

    # Calc and returns output state depending on input state

    def _calc_output_state(self):
        for i in self.get_inputs():
            if self.get_input_state(i) is False:
                return False
        return True
