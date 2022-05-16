__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2022-04-17'

"""
Huffman homework
2022
@author: liam-alexandre.abourousse
"""

from algopy import bintree
from algopy import heap


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
# COMPRESSION

def buildfrequencylist(dataIN):
    """
    Builds a tuple list of the character frequencies in the input.
    """
    # find the frequency of the first character in the string
    frequencylist = []
    for i in range(len(dataIN)):
        if dataIN[i] not in frequencylist:
            frequencylist.append(dataIN[i])
    # find the frequency of the other characters
    for i in range(len(frequencylist)):
        frequencylist[i] = (frequencylist[i], dataIN.count(frequencylist[i]))
    # reverse the order of each tuple
    for i in range(len(frequencylist)):
        frequencylist[i] = (frequencylist[i][1], frequencylist[i][0])
    return frequencylist


def __orderlist(list):
    """
    Orders a list of characters by their frequency.
    """
    # order the list of tuples (frequency, character) by frequency in descending order
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j][0] < list[j + 1][0]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def buildHuffmantree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """

    L = __orderlist(inputList)

    # build the frequency table from the input list
    FrequencyList = []
    CharacterList = []

    for i in range(len(L)):
        FrequencyList.append(inputList[i][0])
        CharacterList.append(inputList[i][1])

    # build the heap

    HeapBintree = heap.Heap()

    # push to the bintree the tuple (frequency, binary tree) the binary tree is a leaf with none as left and right child and the character as key. The heap is built from the highest frequency to the lowest.
    for i in range(len(FrequencyList)):
        HeapBintree.push(
            (FrequencyList[i], bintree.BinTree(CharacterList[i], None, None)))

    counter = 0

    while len(HeapBintree.elts) > 2:
        # always make sure internal nodes have None and not bc

        # pop the two highest frequency trees
        f1, t1 = HeapBintree.pop()
        f2, t2 = HeapBintree.pop()

        # build the new tree with the two trees
        t3 = bintree.BinTree(None, t2, t1)
        t3.key = f1 + f2

        # push the new tree in the heap
        HeapBintree.push((f1 + f2, t3))
        counter += 1

    # return the root of the tree
    return HeapBintree.pop()[1]


def __toBinary(char, length=8):
    """
    Converts a character to its binary representation.
    """
    nombre = ord(char)
    result = ""
    while len(result) < length:
        result = str(nombre % 2) + result
        nombre = nombre // 2
    return result


def __bintodecimal(binary):
    """
    Converts a binary string to its decimal representation.
    """
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2**(len(binary) - 1 - i)
    return decimal


def encodedata(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.
    """
    for char in dataIN:
        string += __encodechar(huffmanTree, char)
    return string


def __encodechar(huffmanTree, char, occ=''):
    """
    Auxiliary function that recursively calls the function to encode a character. The code of characters is a string of 0 and 1, 0 means left and 1 means right.
    """
    if huffmanTree.left == None:  # full => B.right == None
        if huffmanTree.key == char:
            return occ
        else:
            return None
    else:
        res = __encodechar(huffmanTree.left, char, occ+'0')
        if res != None:
            return res
        else:
            return __encodechar(huffmanTree.right, char, occ+'1')


def encodetree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    string = ''
    string = __encodetree(huffmanTree, string)
    return string


def __encodetree(huffmanTree, string):
    """
    Auxiliary function that recursively calls the function to encode a character. The code of characters is a string of 0 and 1, 0 means left and 1 means right.
    """
    # Encodes a huffman tree to its binary representation using a preOrder traversal: * each leaf key is encoded into its binary representation on 8 bits preceded by '1' * each time we go left we add a '0' to the result
    if huffmanTree.left == None:  # full => B.right == None
        string += '1' + __toBinary(huffmanTree.key)
        return string
    else:
        string += '0'
        string = __encodetree(huffmanTree.left, string)
        string = __encodetree(huffmanTree.right, string)
        return string


def tobinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    string = ''
    i = 0
    test = ''
    l = len(dataIN)
    while i < l:
        if(i + 8 < l):
            for j in range(i, i + 8):
                string += dataIN[j]
            test += chr(__bintodecimal(string))
            string = ''
        i += 8
    if i >= 8:
        i = i - 8
        while (i < l):
            string += dataIN[i]
            i += 1
        test += chr(__bintodecimal(string))
    return test, 8 - len(string)


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """

    # get the frequency list
    frequencyList = buildfrequencylist(dataIn)

    # build the huffman tree
    huffmanTree = buildHuffmantree(frequencyList)

    # encode the data
    data1 = encodedata(huffmanTree, dataIn)

    # convert the data to binary
    data1, align1 = tobinary(data1)

    data2 = encodetree(huffmanTree)

    data2, align2 = tobinary(data2)

    return (data1, align1), (data2, align2)


################################################################################
# DECOMPRESSION

def decodedata(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    treehead = huffmanTree
    decodedoutput = ''
    for x in dataIN:
        if x == '1':
            huffmanTree = huffmanTree.right
        elif x == '0':
            huffmanTree = huffmanTree.left
        if huffmanTree.right == None and huffmanTree.left == None:
            decodedoutput += huffmanTree.key
            huffmanTree = treehead
    string = ''
    for item in decodedoutput:
        string += str(item)
    return string


def decodetree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    string, i = __decodetree(dataIN)
    return string

def __decodetree(dataIN, i=0):
    b = bintree.BinTree(None, None, None)
    if i < len(dataIN):
        if dataIN[i] == '0':
            (b.left, i) = __decodetree(dataIN, i+1)
            (b.right, i) = __decodetree(dataIN, i)
            return (b, i)
        else:
            s = ''
            n = 1
            while n <= 8:
                s += dataIN[i+n]
                n += 1
            b.key = chr(__bintodecimal(s))
            return (b, i+n)
    return b, i


def frombinary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    i = 0
    string = ''
    while len(dataIN) - 1 > i:
        string += __toBinary(dataIN[i])
        i += 1
    lenght = __toBinary(dataIN[i])
    while align < len(lenght):
        string += lenght[align]
        align += 1
    return string

def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    data = frombinary(data, dataAlign)
    tree = frombinary(tree, treeAlign)
    tree = decodetree(tree)
    return decodedata(tree, data)