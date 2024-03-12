def detect_hamming_error(codeword):
    # Vérification de la longueur du mot de code
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
    # Vérification de la longueur du mot de code
    if len(data) != 7:
        raise ValueError("Le mot de code doit être de longueur 7.")

    return data[0] + data[1] + data[2] + data[3]


def vigenere_decode(msg: str, key: str) -> str:
    """
    Décode un message avec le chiffrement de Vigenère
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
    with open(filename, "r") as f:
        return f.read()


filename = "file.txt"

# Lire le fichier binaire et convertir en une liste de bits
print("Lecture du fichier binaire")
lettre = read_binary_file(filename)
lettre_corrige = ""
lettre_decode = ""
lettre_decode_ascii = ""

print("dectection et correction des erreurs")
for i in range(0, len(lettre), 7):
    lettre_corrige += detect_hamming_error(lettre[i:i + 7])

print("Décodage du message")
for i in range(0, len(lettre_corrige), 7):
    lettre_decode += decode_hamming(lettre_corrige[i:i + 7])

# transformation de la lettre_decode binaire en ascii
print("Conversion du message en ASCII")
for i in range(0, len(lettre_decode), 8):
    lettre_decode_ascii += chr(int(lettre_decode[i:i + 8], 2))

print("Décodage du message avec le chiffrement de Vigenère")
print(vigenere_decode(lettre_decode_ascii, "PYTHON"))
