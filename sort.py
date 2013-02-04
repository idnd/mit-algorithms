

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



def quickSort(A,p,r,myflag = False):

    def partition(A,p,r,myflag):
        print 'partition a=',A,'p=',p,'r=',r
        x = A[r-1]                      #pivot
        i = p - 1
        for j in xrange(p,r-2):
            if A[j] <= x:
                i = i + 1
                A[i],A[j] = A[j],A[i]
            if myflag:
                print A
        if myflag:
            print (i+1),(r-1)
            print A[i+1], A[r-1]
        A[i+1],A[r-1] = A[r-1],A[i+1]
        if myflag:
            print A[i+1], A[r-1]
            print 'return =', (i + 1)
            print A
        return i + 1
    if p<r-1:
        q = partition(A,p,r,myflag)
        quickSort(A,p,q-1,True)
        quickSort(A,q+1,r,True)

'''
X = [1,5,3,2,4]
X = [2,8,7,1,3,5,6,4]
arrayPrint(X)
quickSort(X, 0,len(X),True)
arrayPrint(X)
'''
import RedBlackTree
