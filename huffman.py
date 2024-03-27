class HuffmanNode:
    # constructor, Time O(1) Space O(1)
    def __init__(self, ch, frequency, left, right):
        """
        Permet de créer un noeud de l'arbre binaire
        :param ch: Caractère
        :param frequency: Fréquence du caractère
        :param left: Fils gauche
        :param right: Fils droit
        """
        self.ch = ch
        self.frequency = frequency
        self.left = left
        self.right = right


class HuffmanCoding:

    def getCode(self, input):
        """
        Permet de coder un message avec l'algorithme de Huffman
        :param input: message à coder
        :return: codeMap : dictionnaire contenant les codes de Huffman
        """
        freqMap = self.buildFrequencyMap(input)
        nodeQueue = self.sortByFrequence(freqMap)
        self.root = self.buildTree(nodeQueue)
        codeMap = self.createHuffmanCode(self.root)
        return codeMap

    # Step 1: Create char frequency map from input string, Time O(s) Space O(m),
    # s is number of chars in input string, m is number of unique chars
    def buildFrequencyMap(self, input):
        """
        Permet de construire une map de fréquence des caractères
        :param input: message à coder
        :return: map : dictionnaire contenant les fréquences des caractères
        """
        map = {}
        for c in input:
            map[c] = map.get(c, 0) + 1
        return map

    # Step 2: Create queue of nodes from map and sort by frequency, Time O(mlogm) Space O(m)
    def sortByFrequence(self, map):
        """
        Permet de trier les fréquences des caractères
        :param map: dictionnaire contenant les fréquences des caractères
        :return: queue : liste des fréquences triées
        """

        queue = []
        for k, v in map.items():
            queue.append(HuffmanNode(k, v, None, None))
        queue.sort(key=lambda x: x.frequency)
        return queue

        # Step 3: Build frequency-sorted binary tree from sorted queue, return root

    # Time O(m) Space O(n), m is unique chars in string, n is nodes in tree n=2m-1
    def buildTree(self, nodeQueue):
        """
        Permet de construire un arbre binaire à partir des fréquences triées
        :param nodeQueue: liste des fréquences triées
        :return: nodeQueue.pop(0) : racine de l'arbre binaire
        """
        while len(nodeQueue) > 1:
            node1 = nodeQueue.pop(0)
            node2 = nodeQueue.pop(0)
            node = HuffmanNode('', node1.frequency + node2.frequency, node1, node2)
            nodeQueue.append(node)
        return nodeQueue.pop(0)

    # Step 4: Create Huffman code map by preorder of the tree, Time O(n) Space O(m+n)
    def createHuffmanCode(self, node):
        """
        Permet de créer un dictionnaire de codes de Huffman
        :param node: racine de l'arbre binaire
        :return: map : dictionnaire de codes de Huffman
        """
        map = {}
        self.createCodeRec(node, map, "")
        return map

    # Preorder of the tree using recursion, Time O(n) Space O(n)
    def createCodeRec(self, node, map, s):
        """
        Permet de créer un dictionnaire de codes de Huffman
        :param node: racine de l'arbre binaire
        :param map: dictionnaire de codes de Huffman
        :param s: code de Huffman
        :return: None
        """
        if node.left == None and node.right == None:
            map[node.ch] = s
            return
        self.createCodeRec(node.left, map, s + '0')
        self.createCodeRec(node.right, map, s + '1')

    # Step 5. Use huffman code to encode the input string, Time O(s) Space O(o),
    # s is input string length, o is output string length
    def encode(self, codeMap, input):
        """
        Permet de coder un message avec l'algorithme de Huffman
        :param codeMap: dictionnaire de codes de Huffman
        :param input: message à coder
        :return: message : message codé
        """
        message = ""
        for i in range(0, len(input)):
            message = codeMap.get(input[i])
        return message

    # Step 6. decode. Time O(o), Space O(s), o is coded message length, s is original message input
    def decode(self, coded):
        """
        Permet de décoder un message avec l'algorithme de Huffman
        :param coded: message codé
        :return: message : message décodé
        """
        message = ""
        curr = self.root
        for i in range(0, len(coded)):
            curr = curr.right if coded[i] == '1' else curr.left
            if curr.left == None and curr.right == None:
                message += curr.ch
                curr = self.root
        return message
