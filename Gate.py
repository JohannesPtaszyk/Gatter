class Gate:
    def __init__(self, input_count):
        self.typ = ""
        self.input_count = input_count
        self.output = False
        self.inputs = []

        # Create an array with the length representing the number of inputs
        # in addition to set all inputs to false
           
        for i in range(0, input_count):
            self.inputs.append(False)

    # Get Gate type

    def get_typ(self):
        return self.typ

    # Get number of Gate inputs

    def get_input_count(self):
        return self.input_count

    # Get array of input states

    def get_inputs(self):
        return self.inputs

    # Get state of a specific input

    def get_input_state(self, index):
        return self.inputs[index]

    # Get state of output

    def get_output_state(self):
        return self.output

    # Set state of a specific input

    def set_input_state(self, index, value):
        try:
            self.inputs[index] = value
        except():
            print("Error while setting input value")

    # Set state of output

    def set_output_state(self, value):
        self.output = value

    # Sets the output state according to the result of calc_output_state

    def refresh_output_state(self):
        self.set_output_state(self.calc_output_state())

    # Placeholder for a method to calculate and change the output depending on the inputs
    # this method has to be overwritten in the subclass

    def calc_output_state(self):
        return "Error: " \
               "Its not possible to get an output of the 'Gate' class, please use a subclass and override this method"

