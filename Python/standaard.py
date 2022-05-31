def filter_unique(arr):
    """
    :param arr: de array die gefilterd moet worden zodat het enkel nog maar unieke elementen bevat
    :return: de array met de unieke elementen
    >>> filter_unique(['a', 'b', 'a', 'c', 'a'])
    ['a', 'b', 'c']
    >>> filter_unique(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> filter_unique("abc")
    ['a', 'b', 'c']
    >>> filter_unique([5, 0, 1, 5, 6, 0, 0])
    [5, 0, 1, 6]
    """
    result = []
    for elem in arr:
        if elem not in result:
            result.append(elem)
    return result
