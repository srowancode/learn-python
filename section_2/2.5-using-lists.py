def using_lists() -> None:
    """Understanding python list container."""

    # initializer for an empty list, square brackets []
    names: list = []

    # initializer lists with entries, variable = [entry1, entry2, ...]
    names: list = ['Scott Rowan', 'Carol Danvers']
    ages: list = [35, 51]

    print(names)
    print(ages)

    # accessing specific values (0-indexed), list[index]
    print(names[0])
    print(ages[1])

    # get length, i.e. number of entries in list
    print(len(names))

    # adding indiviual items to a list, list.append(item)
    names.append('Peter Parker')
    print(names)
    print(len(names))

    # removing indiviual items from a list, list.remove(item)
    names.remove('Carol Danvers')
    print(names)
    print(len(names))

    # concatinating another list, list += another_list
    ages += [57, 79, 14]
    print(ages)

    # accessing last value, list[-1]
    print(ages[-1])

    # accessing subset
    ## note the [from:to] format, return a subset from 'from' up to the item BEFORE 'to'
    print(ages[2:4])

    # to get a subset from a value until the end of the list, use len(ages)
    print(ages[2:len(ages)])


if __name__ == '__main__':
    using_lists()