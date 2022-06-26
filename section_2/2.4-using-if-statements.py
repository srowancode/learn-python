def using_if_statements() -> None:
    """Understanding 'if' conditional statements."""

    name: str = 'Dr. Scott Rowan'
    age: int = 35

    # note the double '==' to check if equal to
    if name == 'Dr. Scott Rowan':
        # this will print
        print('name: ', name)

    # note '!=' to check if not equal to
    if name != 'Dr. Scott Rowan':
        # this will not print
        print('name: ', name)

    # using '>=' is greater than or equal to
    if age >= 30:
        # this will print
        print('age:  ', age)

    # 'not' means do if the following is 'not' true
    ## we cannot use the '!' in this context
    if not age >= 30:
        # this will not print
        print('age:  ', age)

    # working with multiple conditions
    # 'and' example
    if name == 'Dr. Scott Rowan' and age < 30:
        # this will not print, as all conditions need to be true for 'and'
        print(name + ": ", age)

    # 'or' example
    if name == 'Dr. Scott Rowan' or age < 30:
        # this will print, as only 1 needs to be true for 'or'
        print(name + ": ", age)


if __name__ == '__main__':
    using_if_statements()