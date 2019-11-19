"""
This is the search example module

"""

def binarysearch(seq, t):
    """Searches the index i of t in a seq.
    Returns -1 when there is no t in seq.
    The input seq should be sorted. 

    >>> binarysearch([1,10, 100, 200, 1000], 200)
    3
    >>> binarysearch([1,10, 100, 200, 1000], 11)
    -1
    """
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:

        elif seq[m] > t:

        else:
            return m

def linearsearch(seq, item, start=0):
    """Searches the index t (not the value) from seq.
    >>> binarysearch([1,10, 100, 200, 1000], 200)
    3
    >>> binarysearch([1,10, 100, 200, 1000], 11)
    -1
    """
    for i in range(start, len(seq)):


    return -1
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()