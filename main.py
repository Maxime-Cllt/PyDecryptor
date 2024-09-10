from random import random
from huffman import HuffmanCoding


def detect_hamming_error(codeword):
    """
    Permet de détecter et corriger les erreurs dans un mot de code de Hamming
    Complexité : O(1)
    :param codeword: Mot de code de Hamming
    :return: Mot de code de Hamming corrigé
    """

    if len(codeword) != 7:
        raise ValueError("Le mot de code doit être de longueur 7.")

    # Calcul des bits de parité reçus
    p1 = (int(codeword[0]) + int(codeword[1]) + int(codeword[2])) % 2
    p2 = (int(codeword[0]) + int(codeword[1]) + int(codeword[3])) % 2
    p3 = (int(codeword[1]) + int(codeword[2]) + int(codeword[3])) % 2

    p = (p1, p2, p3)
    bit = (int(codeword[4]), int(codeword[5]), int(codeword[6]))

    critere_de_correction = (p[0] == bit[0], p[1] == bit[1], p[2] == bit[2])

    # Vérification de la présence d'erreur

    index_error = -1
    # si c1 faux, c5, c6 faux, c7 vrai
    if critere_de_correction == (False, False, True):
        index_error = 0
    # si c2 faux, c5 vrai, c6, et c7 faux
    elif critere_de_correction == (False, False, False):
        index_error = 1
    #     si c3 faux, c5 et c7 faux et c6 vrai
    elif critere_de_correction == (False, True, False):
        index_error = 2
    #     si c4 faux, c6 et c7 faux et c5 vrai
    elif critere_de_correction == (True, False, False):
        index_error = 3

    if index_error != -1:
        print("error", index_error)

        # Correction de l'erreur
        bit = [int(c) for c in codeword]
        bit[index_error] = 1 - bit[index_error]
        print("Correction", bit)
        return "".join(str(b) for b in bit)

    return codeword


# prend un mot de code de 7 bits et retourne le mot decodé
def decode_hamming(data: str):
    """
    Décode un mot de code de Hamming
    Complexité : O(1)
    :param data:  Mot de code de Hamming
    :return: Mot de code de Hamming décodé
    """
    if len(data) != 7:
        raise ValueError("Le mot de code doit être de longueur 7.")

    return data[0] + data[1] + data[2] + data[3]


def vigenere_decode(msg: str, key: str) -> str:
    """
    Décode un message avec le chiffrement de Vigenère
    Complexité : O(n)
    :param msg: Message à décoder
    :param key: Clé de chiffrement
    :return: Message décodé avec le chiffrement de Vigenère
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    index_cle = 0
    for char in range(len(msg)):
        column = alphabet.find(msg[char].lower())
        row = alphabet.find(key[index_cle].lower())
        if column == -1:
            result += msg[char]
        else:
            if msg[char].isupper():
                result += alphabet[(column - row) % len(alphabet)].upper()
            else:
                result += alphabet[(column - row) % len(alphabet)]
            index_cle = (index_cle + 1) % len(key)
    return result


def read_binary_file(filename):
    """
     Lit un fichier binaire et retourne son contenu
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        return f.read()


def generate_random_key(message):
    """
    Génère une clé aléatoire de longueur donnée
    :param message: Message à chiffrer
    :return: Clé de chiffrement
    """
    cle = ""

    for iLettre in range(len(message)):
        cle += chr(int(random() * 26) + ord('a'))
    return cle


def vernam_encrypt(plaintext):
    """
    Chiffre un message avec le chiffrement de Vernam
    Complexité : O(n)
    :param plaintext: Message à chiffrer
    :return: Message chiffré et clé de chiffrement
    """
    key = generate_random_key(plaintext)
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext, key


def vernam_decrypt(ciphertext, key):
    """
    Déchiffre un message avec le chiffrement de Vernam
    Complexité : O(n)
    :param ciphertext:  Message chiffré
    :param key:  Clé de chiffrement
    :return:  Message déchiffré
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i]))
    return plaintext


if __name__ == '__main__':
    filename = "file.txt"

    # Lire le fichier binaire et convertir en une liste de bits
    lettre = read_binary_file(filename)
    lettre_corrige = ""
    lettre_decode = ""
    lettre_decode_ascii = ""
    lettre_decode_vigenere = ""

    # Détection et correction des erreurs
    print("Détection et correction des erreurs...")
    for i in range(0, len(lettre), 7):
        lettre_corrige += detect_hamming_error(lettre[i:i + 7])

    with open("Etape_1_Lettre_corrige.txt", "w") as f:
        f.write(lettre_corrige)

    # Déchiffrement du message
    print("Déchiffrement du message...")
    for i in range(0, len(lettre_corrige), 7):
        lettre_decode += decode_hamming(lettre_corrige[i:i + 7])

    with open("Etape_2_Lettre_decode.txt", "w") as f:
        f.write(lettre_decode)

    # Conversion du message en ASCII
    print("Conversion du message en ASCII...")
    for i in range(0, len(lettre_decode), 8):
        lettre_decode_ascii += chr(int(lettre_decode[i:i + 8], 2))

    with open("Etape_3_Lettre_decode_ascii.txt", "w") as f:
        f.write(lettre_decode_ascii)

    # Déchiffrement du message avec le chiffrement de Vigenère
    print("Déchiffrement du message avec le chiffrement de Vigenère...")
    lettre_decode_vigenere = vigenere_decode(lettre_decode_ascii, "PYTHON")
    print(lettre_decode_vigenere)

    with open("Etape_4_Lettre_decode_vigenere.txt", "w") as f:
        f.write(lettre_decode_vigenere)

    # Chiffrement du message avec le chiffrement de Vernam
    print("Chiffrement du message avec le chiffrement de Vernam...")
    encrypted_text, key = vernam_encrypt(lettre_decode_vigenere)

    with open("Etape_5_Lettre_chiffrage_vernam.txt", "w") as f:
        f.write(encrypted_text)

    with open("Etape_5_Lettre_chiffrage_vernam_bynary.txt", "w") as f:
        f.write("".join(f"{ord(i):08b}" for i in encrypted_text))

    with open("Etape_5_Cle_vernam.txt", "w") as f:
        f.write(key)
    # print(f"Cle de chiffrement pour le chiffrement de Vernam : \n{key}")

    decrypted_text = vernam_decrypt(encrypted_text, key)

    # Compression du message avec Huffman
    print("Compression du message avec Huffman...")
    huffman = HuffmanCoding()
    codeMap = huffman.get_code(encrypted_text)
    # print("code map : ", codeMap)
    HuffmanCoding.save_huffman_object("huffman_code.txt", huffman)
    huffman = HuffmanCoding.load_huffman_object("huffman_code.txt")
    codeMap = huffman.get_code(encrypted_text)

    # Encodage du message avec Huffman pour la compression
    lettre_encode_verman_huffman = huffman.encode(codeMap, encrypted_text)
    # Décodage du message avec Huffman
    lettre_decode_verman_huffman = huffman.decode(lettre_encode_verman_huffman)
    # Déchiffrement du message avec le chiffrement de Vernam après Huffman
    lettre_decode_verman_huffman_decrypted = vernam_decrypt(lettre_decode_verman_huffman, key)

    with open("Etape_6_Lettre_encode_verman_huffman.txt", "w") as f:
        f.write(lettre_encode_verman_huffman)

    with open("Etape_7_Lettre_decode_verman_huffman.txt", "w") as f:
        f.write(lettre_decode_verman_huffman)

    with open("Etape_8_Lettre_decode_verman_huffman_decrypted.txt", "w") as f:
        f.write(lettre_decode_verman_huffman_decrypted)

    # print(
    #     f"Message crypté avec le chiffrement de Vernam et compressé avec Huffman en binaire: \n{lettre_encode_verman_huffman}")
    # print(f"taille message original : {len(lettre_decode_vigenere) * 8} bits")
    # print(f"taille message compressé : {len(lettre_encode_verman_huffman)} bits")
    print(f"Taux de compression : {len(lettre_decode_vigenere) * 8 / len(lettre_encode_verman_huffman)}")
    print("Fin du programme")
