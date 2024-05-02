import pickle


class HuffmanNode:
    # constructor, Time O(1) Space O(1)
    def __init__(self, ch, frequency, left, right):
        """
        Permet de créer un noeud de l'arbre de Huffman
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

    # All steps to create huffman code
    def __init__(self):
        self.root = None

    def getCode(self, input):
        """
        Permet de créer un code Huffman
        :param input: La chaine de caractère à encoder
        :return: Le code Huffman
        """
        freqMap = self.buildFrequencyMap(input)
        nodeQueue = self.sortByFrequence(freqMap)
        self.root = self.buildTree(nodeQueue)
        codeMap = self.createHuffmanCode(self.root)
        return codeMap

    def buildFrequencyMap(self, input):
        """
        Permet de construire la fréquence des caractères
        :param input:  La chaine de caractère à encoder
        :return:  La fréquence des caractères
        """
        map = {}
        for c in input:
            map[c] = map.get(c, 0) + 1
        return map

    def sortByFrequence(self, map):
        """
        Permet de trier les fréquences des caractères
        :param map: La fréquence des caractères
        :return: La fréquence des caractères triée
        """
        queue = []
        for k, v in map.items():
            queue.append(HuffmanNode(k, v, None, None))
        queue.sort(key=lambda x: x.frequency)
        return queue

        # Step 3: Build frequency-sorted binary tree from sorted queue, return root

    def buildTree(self, nodeQueue):
        """
        Permet de construire l'arbre binaire trié par fréquence
        :param nodeQueue:  L'arbre binaire trié par fréquence
        :return: L'arbre binaire trié par fréquence
        """
        while len(nodeQueue) > 1:
            node1 = nodeQueue.pop(0)
            node2 = nodeQueue.pop(0)
            node = HuffmanNode('', node1.frequency + node2.frequency, node1, node2)
            nodeQueue.append(node)
        return nodeQueue.pop(0)

    def createHuffmanCode(self, node):
        """
        Permet de créer le code Huffman
        :param node: Le noeud de l'arbre de Huffman
        :return: Le code Huffman
        """
        map = {}
        self.createCodeRec(node, map, "")
        return map

    def createCodeRec(self, node, map, s):
        if node.left is None and node.right is None:
            map[node.ch] = s
            return
        self.createCodeRec(node.left, map, s + '0')
        self.createCodeRec(node.right, map, s + '1')

    def encode(self, codeMap, input):
        """
        Permet d'encoder le message
        :param codeMap: Le code Huffman
        :param input:  La chaine de caractère à encoder
        :return: Le message encodé
        """
        s = ""
        for i in range(0, len(input)):
            s += codeMap.get(input[i])
        return s

    def decode(self, coded):
        """
        Permet de décoder le message
        :param coded: Le message encodé
        :return: Le message décodé
        """
        s = ""
        curr = self.root
        for i in range(0, len(coded)):
            curr = curr.right if coded[i] == '1' else curr.left
            if curr.left is None and curr.right is None:
                s += curr.ch
                curr = self.root
        return s

    @staticmethod
    def saveHuffmanObject(filename, obj):
        """
        Permet de sauvegarder la classe HuffmanCoding ainsi que tout les attributs
        :param filename: Le nom du fichier
        """
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def loadHuffmanObject(filename):
        """
        Permet de charger un objet HuffmanCoding depuis un fichier
        :param filename: Le nom du fichier
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)
