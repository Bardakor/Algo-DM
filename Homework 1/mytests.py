# Special Python function to load module with its file name
from importlib.machinery import SourceFileLoader
import time

# My handout
myfile = "liam-alexandre.abourousse_heaps .py"
# Load module. Same result as "import mycode"
mycode = SourceFileLoader('mycode', myfile).load_module()

start = time.time()


def tests_is_empty():
    """
    Write a function that test if the function isEmpty in mycode.py is working correctly. Adding other heaps to the test.
    """
    H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'),
         (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
    assert mycode.is_empty(H) == False
    H = [None]
    assert mycode.is_empty(H) == True


"""
Write a function that test if the function heap_push in mycode.py is working correctly. Adding other heaps to the test.
"""


def tests_heap_push():
    """
    Write a function that test if the function heap_push in mycode.py is working correctly. Adding other heaps to the test.
    """
    H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'),
         (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
    mycode.heap_push(H, 'N', 5)
    assert H == [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (
        10, 'B'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
    H = [None]
    mycode.heap_push(H, 'N', 5)
    assert H == [None, (5, 'N')]
    # Code of the docs
    H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'),
         (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
    mycode.heap_push(H, 'N', 5)
    assert H == [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (
        10, 'B'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
    H = [None]
    mycode.heap_push(H, "newelt", 42)
    assert H == [None, (42, 'newelt')]


def tests_heap_pop():
    """
    Write a function that test if the function heap_pop in mycode.py is working correctly. Adding other heaps to the test.
    """
    # Test from docs:
    H = [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'),
         (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
    assert mycode.heap_pop(H) == (2, 'A')
    assert H == [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'),
                 (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
    H = [None, (11, 'e_2'), (11, 'e_4'), (11, 'e_5'), (16, 'e_7'), (13, 'e_3'),
         (27, 'e_1'), (27, 'e_6'), (40, 'e_0'), (26, 'e_8'), (36, 'e_9')]
    assert mycode.heap_pop(H) == (11, 'e_2')
    assert H == [None, (11, 'e_4'), (13, 'e_3'), (11, 'e_5'), (16, 'e_7'),
                 (36, 'e_9'), (27, 'e_1'), (27, 'e_6'), (40, 'e_0'), (26, 'e_8')]
    assert mycode.heap_pop(H) == (11, 'e_4')
    assert H == [None, (11, 'e_5'), (13, 'e_3'), (26, 'e_8'), (16, 'e_7'),
                 (36, 'e_9'), (27, 'e_1'), (27, 'e_6'), (40, 'e_0')]


def tests_is_heap():
    """
    Write a function that test if the function tests_is_heap in mycode.py is working correctly. Adding other heaps to the test.
    """
    # Tests from docs:
    H = [None]
    assert mycode.is_heap(H) == True

    H = [None, (3, 'A'), (2, 'B'), (1, 'C')]
    assert mycode.is_heap(H) == False
    H = [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'),
         (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
    assert mycode.is_heap(H) == True


def tests_heap_sort():
    """
    Write a function that test if the function heap_sort in mycode.py is working correctly. Adding other heaps to the test.

    H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'),
         (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
    res = mycode.heap_sort(H)
    assert res == [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'),
                   (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
     """
    # Tests from docs:
    L = [('A', 20), ('B', 5), ('C', 10), ('D', 12), ('E', 15),
         ('F', 8), ('G', 2), ('H', 6), ('I', 2), ('J', 9)]
    l = mycode.heap_sort(L)
    assert l == [('G', 2), ('I', 2), ('B', 5), ('H', 6), ('F', 8),
                 ('J', 9), ('C', 10), ('D', 12), ('E', 15), ('A', 20)]
    L = []
    assert mycode.heap_sort(L) == []


tests_is_empty()
tests_heap_push()
tests_heap_pop()
tests_is_heap()
tests_heap_sort()
end = time.time()

print("All tests passed in " + str(round(end - start, 10)) +
      " seconds!\nIncluding:\n - is_empty,\n - heap_push,\n - heap_pop,\n - is_heap,\n - heap_sort.")
