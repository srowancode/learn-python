def working_with_numbers() -> None:
    """Understand how to carry out simple operations with numbers."""

    # Number variables are of type 'int', here are some simple math operations
    value_1: int = 1
    value_2: int = 4
    print(value_1 + value_2)
    print(value_1 - value_2)
    print(value_1 * value_2)
    print(value_1 / value_2)

    # note that divide prints 0.25, a value with a decimal point is no longer an 'int'
    # numbers values with decimal are of type 'float'
    ## you can ensure a value without a decimal is a float using the 'float(value)' function 
    ### we can check the type of a variable using the 'type(value)' function
    value_1: int = 1
    decimal_value_1: float = 0.25

    value_2: float = 1
    decimal_value_2: float = float(1)
    print(value_1)
    print(type(value_1)) # will show type to be of class 'int'

    print(decimal_value_1)
    print(type(decimal_value_1)) # will show type to be of class 'float'

    print(value_2) # note the added decimal place!!!
    print(type(value_2)) # you might expect to show int, but will show float

    print(decimal_value_2)
    print(type(decimal_value_2)) # will show float

    # similarly you can ensure a value is of type int
    ## note that this is not advised as it just removes the decimal, i.e. rounds down
    print(int(2.2)) # prints 2
    print(int(2.7)) # still only prints 2, i.e. round down

    # to round up you could do the add one before you call the int function
    ## note that this is not advised as it is not obvious what you are doing
    print(int(2.2 + 1))
    
    # to round up / down safely, use the in-built floor and ceil functions from the math library
    import math

    print(math.floor(2.2))
    print(math.ceil(2.2))

    # the modulo operator '%'
    # the '%' operator carries out a division and return the remainder
    # the '%' operator is especially useful for indentifying if a value is odd or even
    # e.g. value % 2 would return 0 if value is even and 1 if value is odd
    print(4 % 2) # 4 / 2 = 2 remainder 0, so prints 0, even number
    print(5 % 2) # 4 / 2 = 2 remainder 1, so prints 1, odd number


if __name__ == '__main__':
    working_with_numbers()