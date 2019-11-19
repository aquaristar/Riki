'''
This is a simple test module to demonstrate Python's doctest features. 

It tests three functions:
1. bubblesort
2. insertionsort
3. quicksort
'''

def bubblesort(x):
    """
    >>> bubblesort([3,1,2,7,6,5,4])
    [1, 2, 3, 4, 5, 6, 7]
    """
    length = len(x)-1
    for i in range(length):
        for j in range(length-i):
            if x[j] > x[j+1]:

    return x

def insertionsort(x):
    """
    >>> insertionsort([3,1,2,7,6,5,4])
    [1, 2, 3, 4, 5, 6, 7]
    """
    for i in range(1, len( )):
        j = i - 
        key = x[i]
        while x[j] > key and j >= :
            x[j+1]  = x[j]
            j = j - 
        x[j+1] = key
    return x

def quicksort(x):
    """
    >>> quicksort([3,1,2,7,6,5,4])
    [1, 2, 3, 4, 5, 6, 7]
    """
    if len(x) > 1:
        pivot = x[len(x) - ]
        left, mid, right = [], [], []
        for i in range(len(x) - ):
            if x[i] < pivot:
                left.append(x[i])
            elif x[i] > pivot:
                right.append(x[i])
            else:
                mid.append(x[i])
        mid.append(pivot)
        return quicksort(   ) +    + quicksort()
    else:
        return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()