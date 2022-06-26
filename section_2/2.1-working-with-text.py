def working_with_text() -> None:
    """Understand how to carry out simple operations with text strings."""

    # text variables are of type 'str', i.e. string, and are surrounded by quotation marks
    first_name: str = 'Scott'
    print(first_name)
    print(type(first_name))

    # also, make sure not to confuse the type of number which is a written as a string
    number: int = 1
    number_str: str = '1'
    print(type(number))
    print(type(number_str))

    # printing multiple strings together, ',' seperator in print()
    first_name: str = 'Scott'
    last_name: str = 'Rowan'
    print(first_name, last_name)

    # concatonating (adding) strings together and printing as one
    ## note the need to manually add spaces if not included in original
    first_name: str = 'Scott'
    last_name: str = 'Rowan'
    title: str = 'Dr.'
    full_name: str = title + ' ' + first_name + ' ' + last_name
    print(full_name)


if __name__ == '__main__':
    working_with_text()