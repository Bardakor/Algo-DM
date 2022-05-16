__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: heap.py 2022-03-20'

"""
Heap homework
2022 - S2
@author: liam-alexandre.abourousse
"""

# given function


def Heap():
    """ returns a fresh new empty heap

       :rtype: list (heap)
    """
    return [None]

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import


def is_empty(H):
    """ tests if the heap H is empty

       :param H: the heap
       :type H: list (hierarchical rep. of bintree)
       :rtype: bool
    """
    # true if Heap is empty, false otherwise
    return len(H) == 1


def heap_push(H, elt, val):
    """ adds the pair (val, elt) to heap H (in place: no need to return H)

       :param H: The heap
       :type H: list (hierarchical rep. of bintree)
       :param elt: The element to add
       :type elt: any
       :param val: The value associated to elt
       :type val: int or float
    """
    H.append((val, elt))
    __heap_up(H, len(H)-1)


def heap_pop(H):
    """ removes and returns the pair of smallest value in the heap H
    raises Exception if H is empty

       :param H: The heap
       :type H: list (hierarchical rep. of bintree)
       :rtype: (num, any) (the removed pair)
    """
    if is_empty(H):
        raise Exception("Heap is empty")
    else:
        res = H[1]
        H[1] = H[len(H)-1]
        H.pop(len(H)-1)
        __heap_down(H, 1)
        return res


def __heap_up(H, i):
    # move element at index i up in the heap H
    if i == 1:
        return
    else:
        if H[i][0] < H[i//2][0]:
            H[i], H[i//2] = H[i//2], H[i]
            __heap_up(H, i//2)
        else:
            return


def __heap_down(H, i):
    # move element at index i down in the heap H
    if i*2 + 1 > len(H):
        return
    elif 2*i + 1 < len(H):
        if H[i][0] > H[2*i][0] or H[i][0] > H[2*i + 1][0]:
            if H[2 * i][0] > H[2*i + 1][0]:
                H[i], H[2*i + 1] = H[2*i+1], H[i]
                __heap_down(H, 2*i + 1)
            else:
                H[i], H[2*i] = H[2*i], H[i]
                __heap_down(H, 2*i)
    else:
        if H[2*i][0] < H[i][0]:
            H[2*i], H[i] = H[i], H[2*i]


# ---------------------------------------------------------------


def is_heap(T):
    """ tests whether the complete tree T is a heap

       :param T: a complete tree in hierarchical representation
       :type T: list (hierarchical rep. of bintree)
       :rtype: bool
    """
    if T == []:
        return False
    if T == [None]:
        return True
    i = len(T) - 1
    while i > 1 and T[i][0] >= T[i//2][0]:
        i -= 1
    return i == 1


def heap_sort(L):
    """ sorts the associative list of (elements, values) L in increasing order according to values (not in place)

        :param L: a list containing pairs (element: any, value: int)
        :rtype: (any, num) list (the new list sorted)
    """
    #heap_sort algorithm
    H = Heap()
    R = []
    for i in range(len(L)):
        heap_push(H, L[i][0], L[i][1])
    res = []
    while not is_empty(H):
        res.append(heap_pop(H))
    for (elt, val) in res:
        R.append((val, elt)) 
    return R 
    
    
    
    
    
    # #heap_sort algorithm
    # #invert values and elements after building the list
    # L = [(elt, val) for val, elt in L]
    # #build heap
    # for i in range(len(L)//2, 0, -1):
    #     __heap_down(L, i)
    # #sort
    # for i in range(len(L)-1, 0, -1):
    #     L[0], L[i] = L[i], L[0]
    #     __heap_down(L, 1)
    # #invert values and elements
    # L = [(elt, val) for val, elt in L]
    # return L
    
    
    
    
    
    # H = Heap()
    # for elt in L:
    #     heap_push(H, elt[0], elt[1])
    # res = []
    # while not is_empty(H):
    #     res.append(heap_pop(H))
    # return res
