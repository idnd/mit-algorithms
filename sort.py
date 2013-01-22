
def arrayPrint(A):
    for i in xrange( len( A) ):
        print A[i] ,
    print ''
    
def less(a,b):
    return a < b
    
def greater(a,b):
    return a > b
    
def insertionSort(A, func = less):
    """
    Insertion sort:
    - Simple implementation
    - Efficient for (quite) small data sets
    - Adaptive (i.e., efficient) for data sets that are already substantially
    sorted: the time complexity is O(n + d), where d is the number of inversions
    - More efficient in practice than most other simple quadratic (i.e., O(n2)) 
    algorithms such as selection sort or bubble sort; the best case (nearly 
    sorted input) is O(n)
    - Stable; i.e., does not change the relative order of elements with 
    equal keys
    - In-place; i.e., only requires a constant amount O(1) of additional
    memory space
    - Online; i.e., can sort a list as it receives it
    """
    
    for i in xrange( len(A) ):
        valueToInsert = A[i]
        holePos = i
        while holePos > 0 and func(valueToInsert, A[holePos-1]):
            A[holePos] = A[holePos - 1]
            holePos = holePos - 1
        A[holePos] = valueToInsert
        

X = [1,5,3,2,4]
arrayPrint(X)
insertionSort(X, greater)
arrayPrint(X)