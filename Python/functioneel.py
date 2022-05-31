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

def filter_predicate(arr, pred):
    """
    >>>filter_predicate([1, 2, 2, 3, 4, 5, 6, 7, 9, 8], lambda x: x % 2 == 0)
    [2, 2, 4, 6, 8]
    :param arr: de te filteren array
    :param pred: een lambda dat een predicaat voorstelt
    :return: de gefilterde array
    """
    result = []
    for elem in arr:
        if pred(elem):
            result.append(elem)
    return result
