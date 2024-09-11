<h1 align="center">PyDecryptor</h1>

## Scénario

Dans les archives de Claude Shannon, Richard Hamming a retrouvé une lettre dont le contenu se
trouve dans le fichier lettre.txt. Chaque caractère de cette lettre
appartient à la table ASCII et est encodée sur 8 bits. Ne parvenant pas à la déchiffrer, il souhaite
l'envoyer à son ami David Albert Huffman. Sachant que des erreurs pourraient s'insérer dans la lettre
lors de sa transmission, il enrichit le codage binaire (il devient 1,75 fois plus long) pour que le
destinataire puisse éventuellement corriger ces erreurs lors de sa réception.
Une fois la lettre reçue, Huffman détecte deux erreurs (une au début et une à la fin), les corrige, puis
supprime les bits de contrôle et l'encode sous forme de caractères alphanumériques. Obtenant une
suite de caractères incohérents, il se rend compte, après analyse, qu'elle a été chiffrée par une méthode
de chiffrement polyalphabétique du XVIème siècle. Grand amateur de serpents, il parvient à la décrypter
et découvre alors le destinataire de cette lettre.
Decidé à lui faire parvenir, il rechiffre la lettre par une variante du chiffrement précédant, considéré
comme "le seul algorithme cryptographique à confidentialité parfaite" par Claude Shannon. De plus,
jugeant le poids du fichier trop important, il parvient à rendre le codage binaire optimal et à réduire ce
poids de plus d'un quart.
Il envoie alors la lettre chiffrée et compressée à son destinataire, qui parvient finalement à la lire
(grâce aux données supplémentaires que lui a fourni Huffman) ...

## Langage utilisé

- Python

## Prérequis

- Python >=3.10

## Installation

```bash 
git clone https://github.com/Maxime-Cllt/PyDecryptor.git
```

## Utilisation

```bash
python main.py
```

## Auteurs

<ul>
      <li>
        <a
          href="https://github.com/Maxime-Cllt"
        >
          <p>Maxime COLLIAT</p>
        </a>
      </li>
      <li>
        <a
          href="https://github.com/Sudo-Rahman"
        >
          <p>Rahman YILMAZ</p>
        </a>
      </li>
</ul>
