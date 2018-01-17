from Gate import *

if __name__ == '__main__':
    or1 = OR(3)
    or1.set_input_state(0,True)
    or1.refresh_output_state()
    print(or1.get_output_state())

    and1 = AND(3)
    and1.set_input_state(0,True)
    and1.set_input_state(1,True)
    and1.set_input_state(2,True)
    and1.refresh_output_state()
    print(and1.get_output_state())
