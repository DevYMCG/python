def sets():
    set1 = {"apple", "banana", "cherry"}
    set2 = {1, 5, 7, 9, 3}
    set3 = {True, False, False}

    # Operaciones

    """union"""
    set4 = set1 | set2 | set3
    print(set4)

    # output {False, 1, 3, 5, 7, 9, 'apple', 'banana', 'cherry'}

    """Intersección"""
    set5 = set1 & set2 & set3
    print(set5)

    # output set()

    """Diferencias"""
    set6 = set1 - set2
    print(set6)

    # output {'cherry', 'banana', 'apple'}

    """Diferencia Simétrica"""
    set7 = set1 ^ set2
    print(set7)

    # output {1, 3, 'apple', 5, 'banana', 7, 'cherry', 9}


if __name__ == "__main__":
    sets()