def working_with_functions() -> None:
    """Understanding python functions."""

    # functions in python are defined with the 'def' keyword
    # format: def function_name(input1, input2, ...) -> return_type:
    def hello_world_function() -> None:
        """Print Hello World."""

        # prints the provided text to the command window
        print('Hello, World!')
    
    # to call a function we simply use the function name followed by curved brackets ()
    hello_world_function()

    # functions may have inputs, called input arguments:
    def hello_with_specified_input(input_message: str) -> None:
        """Print input message."""

        # prints the provided text to the command window
        print(input_message)

    # define message
    my_message = 'Hello, using an input argument'
    # function call
    hello_with_specified_input(my_message)

    # functions may also return values
    # e.g.
    def hello_function_with_return() -> str:
        """Returns message."""
    
        my_message = 'Hello, using a returned value'
        return my_message

    # the function itself does not print, so we store the return value in a variable
    # message, and then print that instead!
    message = hello_function_with_return()
    print(message)

    # e.g. with int inputs and return int
    def muliply_two_values(value_1: int, value_2: int) -> int:
        """Returns multiplication of inputs value_1 and value_2."""
    
        return value_1 * value_2

    print(muliply_two_values(2, 3))


if __name__ == '__main__':
    working_with_functions()