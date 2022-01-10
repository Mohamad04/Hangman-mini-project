def BinarySearch(L,target):
    first = 0
    last = len(L) - 1
    
    while first <= last:
        midpoint = (first + last) //2

        if L[midpoint] == target:
            return midpoint
        elif L[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


# L = [ 2, 0, 7, 3, 15, 5, 8, 4, 1, 10, 22 ]
# L.sort()
# print(L)
# print( BinarySearch(L, 10) )