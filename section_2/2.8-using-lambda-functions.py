def using_lambda_functions():
    """Understanding python lambda functions."""

    # lambda functions are temporary functions you assign to a
    # local variable which can only be used in the location it was
    # created. using lambda functions is the same as normal function
    # calls, i.e. function_name(input) 

    # The following normal and lambda functions are identical
    ## both take an input value and multiplies it by 2
    def my_normal_function(val) -> int:
        return val * 2

    print(my_normal_function(2))
    print(my_normal_function(4))

    ## note the variable type is 'function'
    my_lambda_function = lambda val: val * 2
    print(type(my_lambda_function))
    print(my_lambda_function(2))
    print(my_lambda_function(4))

    # my_lambda_function takes 2 inputs value and multiplies them
    def my_normal_function(val, val2):
        return val * val2

    my_lambda_function = lambda val, val2: val * val2
    print(my_lambda_function(2, 4))
    print(my_lambda_function(4, 5))

    # why not just use normal functions???
    
    # lambda functions are typically used when you only need to use a
    # function once, as you don't even need to give it a name

    # anonymous lambda functions use format (lambda x: function)(input), e.g.
    val_1: float = 1
    print((lambda x: x * 3)(val_1))

    str_1: str = 'Hello'
    print((lambda x: len(x) * 2)(str_1))

    # lambda functions can also be used to create template functions,
    # a very powerful technique! example:
    
    # create template function for multiplying by a value
    def template_function(input) -> callable:
        return lambda val: val * input
    
    # create two lambda functions according to input
    multiply_by_2 = template_function(2)
    multiply_by_3 = template_function(3)

    print(multiply_by_2(3))
    print(multiply_by_3(3))


if __name__ == '__main__':
    using_lambda_functions()