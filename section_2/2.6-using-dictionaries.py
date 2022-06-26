def using_dictionaries() -> None:
    """Understanding python dictionary containers."""

    # initializer for an empty dictionary, curly brackets {}
    data: dict = {}

    # dictionary entries must have both a key and a value, keys must be unique 
    ## initializer lists with entries, variable = {key1: value1, key2: value2, ...}
    data: dict = {"Scott Rowan": 35, "Carol Danvers": 51}
    print(data)

    # you can also access all key:value pairs via dict.items()
    ## this is more useful when using loops (e.g. in next section 'using loops')
    print(data.items())

    # access specific values given key
    print(data["Carol Danvers"])

    # access keys list
    print(data.keys())
    print(type(data.keys()))

    # access values list
    print(data.values())
    print(type(data.values()))

    # updating value give key
    data["Scott Rowan"] = 21
    print(data.items())

    # adding new entries to a dictionary
    data["Peter Parker"] = 21
    print(data.items())

    # removing entries from a dictionary
    del data["Carol Danvers"]
    print(data.items())


if __name__ == '__main__':
    using_dictionaries()