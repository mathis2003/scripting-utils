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

# python ingebouwde filter kan je ook gebruiken:
filter_obj = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 5, 6, 7, 8])
# merk op dat filter_obj GEEN array is of wat dan ook, maar er kan wel over gelooped worden
for elem in filter_obj:
    print(elem)
