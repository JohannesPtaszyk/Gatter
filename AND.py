from Gate import *

# A Subclass of Gate defining an AND Gate


class AND(Gate):
    def __init__(self, input_count):
        super().__init__(input_count)
        self.typ = "COR"
        
    # Calc and returns output state depending on input state

    def calc_output_state(self):
        for i in range(0,self.get_input_count()):
            if self.get_input_state(i) is True:
                return True
        return False
