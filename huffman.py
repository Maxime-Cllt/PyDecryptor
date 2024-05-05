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

    def __init__(self):
        self.root = None

    def get_code(self, input):
        """
        Permet de créer un code Huffman
        :param input: La chaine de caractère à encoder
        :return: Le code Huffman
        """
        freq_map = self.build_frequency_map(input)
        node_queue = self.sort_by_frequence(freq_map)
        self.root = self.build_tree(node_queue)
        code_map = self.create_huffman_code(self.root)
        return code_map

    def build_frequency_map(self, input):
        """
        Permet de construire la fréquence des caractères
        :param input:  La chaine de caractère à encoder
        :return:  La fréquence des caractères
        """
        map = {}
        for c in input:
            map[c] = map.get(c, 0) + 1
        return map

    def sort_by_frequence(self, map):
        """
        Permet de trier les fréquences des caractères
        :param map: La fréquence des caractères
        :return: La fréquence des caractères triée
        """
        list = []
        for first, second in map.items():
            list.append(HuffmanNode(first, second, None, None))
        list.sort(key=lambda x: x.frequency)
        return list


    def build_tree(self, node_queue):
        """
        Permet de construire l'arbre binaire trié par fréquence
        :param node_queue:  L'arbre binaire trié par fréquence
        :return: L'arbre binaire trié par fréquence
        """
        while len(node_queue) > 1:
            node1 = node_queue.pop(0)
            node2 = node_queue.pop(0)
            node = HuffmanNode('', node1.frequency + node2.frequency, node1, node2)
            node_queue.append(node)
        return node_queue.pop(0)

    def create_huffman_code(self, node):
        """
        Permet de créer le code Huffman
        :param node: Le noeud de l'arbre de Huffman
        :return: Le code Huffman
        """
        map = {}
        self.create_code_rec(node, map, "")
        return map

    def create_code_rec(self, node, map, s):
        if node.left is None and node.right is None:
            map[node.ch] = s
            return
        self.create_code_rec(node.left, map, s + '0')
        self.create_code_rec(node.right, map, s + '1')

    def encode(self, code_map, input):
        """
        Permet d'encoder le message
        :param code_map: Le code Huffman
        :param input:  La chaine de caractère à encoder
        :return: Le message encodé
        """
        s = ""
        for i in range(0, len(input)):
            s += code_map.get(input[i])
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
    def save_huffman_object(filename, obj):
        """
        Permet de sauvegarder la classe HuffmanCoding ainsi que tout les attributs
        :param filename: Le nom du fichier
        """
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def load_huffman_object(filename):
        """
        Permet de charger un objet HuffmanCoding depuis un fichier
        :param filename: Le nom du fichier
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)
