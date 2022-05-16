import unittest
from test import *
from random import *
import random

class MyTestCase(unittest.TestCase):

    def test_empty(self):
        H = Heap()
        self.assertTrue(is_empty(H))


    def test_push(self):
        """H = Heap()
        H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'),
             (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
        heap_push(H, 'N', 5)
        self.assertEqual(H, [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'),
                        (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')])
        heap_push(H, 'Z', 999)
        self.assertEqual(H, [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'),
                        (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F'), (999, 'Z')])
        H2 = Heap()
        heap_push(H2, "newelt", 42)
        self.assertEqual(H2, [None, (42, 'newelt')])"""
        H = Heap()
        for i in range(100, 0, -1):
            heap_push(H, chr(randint(ord("A"), ord("Z"))), i)
            self.assertEqual(H[1][0], i)


    def test_pop(self):
        """H = Heap()
        H = [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'),
 (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
        heap_pop(H)
        self.assertEqual(H, [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'),
  (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')])
        H2 = Heap()
        H2 = [None, (42, 'newelt')]
        heap_pop(H2)
        self.assertEqual(H2, [None])
        with self.assertRaises(Exception):
            heap_pop(H2)
        """
        H = Heap()
        for i in range(100, 0, -1):
            heap_push(H, chr(randint(ord("A"), ord("Z"))), i)
        for i in range(1, 100+1):
            self.assertEqual(heap_pop(H)[0], i)
    

    def test_pop_push(self): 
        """test de noé
        """
        H = Heap()
        x = []
        for i in range(10000):
            try:
                rand = random.randint(1, 42444)
            except Exception:
                pass
        

        heap_push(H, 'e_'+str(i), rand)
        for i in range(10000):
            try:
                elem = heap_pop(H)
                x.append(elem[0])
            except Exception:
                pass
        test = x.copy()
        test.sort()
        self.assertTrue(x == test)


    def test_heap(self):
        """test on multiple heaps
        """
        H1 = [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'),
              (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
        H2 = [None, (3, 'A'), (2, 'B'), (5, 'C')]
        H3 = Heap()
        H4 = [None, (5, 'N'), (12, 'C'), (10, 'B'), (99, 'I'), (16, 'E'), (14, 'D'), (18, 'F'),
              (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
        H5 = [None, (5, 'H'), (5, 'h'), (5, 's'), (5, 'z'), (5, 'H'), (5, 'm'), (5, 'e')]
        H6 = [None, (18, 'b'), (2, 'd')]
        H7 = [None, (5, 'H'), (5, 'h'), (100, 's'), (5, 'z'), (5, 'H'), (200, 'm'), (200, 'e')]
        H8 = [None, (5, 'N')]
        self.assertTrue(is_heap(H1))
        self.assertFalse(is_heap(H2))
        self.assertTrue(is_heap(H3))
        self.assertFalse(is_heap(H4))
        self.assertTrue(is_heap(H5))
        self.assertFalse(is_heap(H6))
        self.assertTrue(is_heap(H7))
        self.assertTrue(is_heap(H8))


    def test_sort(self):
        for _ in range(10):
            L = []
            for _ in range(20):
                c, i = chr(randint(ord("A"), ord("Z")+1)), randint(0, 1000)
                for t in L:
                    while i == t[1]:
                        i = randint(0, 1000)
                L.append((c, i))
            sL = heap_sort(L)
            self.assertEqual(sL, sorted(L, key=lambda t: t[1]))


    # def test_100000(self):
    #     #Test the sort function on 100000 elements (my time 166s), be carefull.
    #     L = []
    #     print("started")
    #     for _ in range(100000):
    #         c, i = chr(randint(ord("A"), ord("Z")+1)), randint(0, 100000)
    #         for t in L:
    #             while i == t[1]:
    #                 i = randint(0, 100000)
    #         L.append((c, i))
    #     #print(L)
    #     sL = heap_sort(L)
    #     #print(sL)
    #     self.assertEqual(sL, sorted(L, key=lambda t: t[1]))
         


if __name__ == '__main__':
    unittest.main()




#Credit : Me, a smart man and a bit of Noé