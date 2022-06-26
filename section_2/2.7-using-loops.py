def using_loops() -> None:
    """Understanding common python loop operations."""

    # quite often you wish to do something for every entry in a list
    # for such a task, we use loops

    # consider the following random value list:
    values: list = [12, 4, 61, 32, 83, 9, 122]

    # 'for loop' with values
    for value in values:
        print(value)

    # example with a dictionary, via dict.items()
    data: dict = {"Scott Rowan": 35, "Carol Danvers": 51}
    for item in data.items():
        print(item)

    # you may also use the follow alternative syntax (way of writing)
    ## the following does the exact same as above
    [print(value) for value in values]

    # python also allows you to use the loops within list brackets to
    # create new lists, operations can be applied
    new_values: list = [(value + 1) for value in values]
    print(new_values)

    # for loop with indexes via range()
    for i in range(len(values)):
        print(values[i])

    # for loop with values and indexes via enumerate()
    for i, value in enumerate(values):
        print(value, values[i] + 1)

    # while loops, i.e. do something while a condition remains true
    ## example, while values is not empty, remove last entry
    while len(values) != 0:
        print(values)
        values.remove(values[-1])


if __name__ == '__main__':
    using_loops()