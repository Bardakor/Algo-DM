# -*- coding: utf-8 -*-
"""
Huffman Tree built for Huffman Homework 'Full Example'
"""

from algopy.bintree import BinTree

HT = BinTree(None,
             BinTree(None, 
                     BinTree(None, 
                             BinTree('m', None, None),
                             BinTree(None,
                                     BinTree(None, 
                                             BinTree('s', None, None),
                                             BinTree('i', None, None)
                                             ),
                                     BinTree('u', None, None)
                                     )
                            ),
                     BinTree('a', None, None)
                     ),
             BinTree(None,
                     BinTree(' ', None, None),
                     BinTree(None,
                             BinTree(None,
                                     BinTree('n', None, None),
                                     BinTree('f', None, None)
                                     ),
                             BinTree('h', None, None)
                             )
                    )
            )


