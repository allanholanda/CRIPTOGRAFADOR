password = 1234
def cripto(frase):
    tradutor = ""

    for letra in frase:

        if letra in "Aa":
            tradutor = tradutor + "@"

        elif letra in "Bb":
            tradutor = tradutor + "#"

        elif letra in "Cc":
            tradutor = tradutor + "&"

        elif letra in "Dd":
            tradutor = tradutor + "%"

        elif letra in "Ee":
            tradutor = tradutor + "$"

        elif letra in "Ff":
            tradutor = tradutor + "1"

        elif letra in "Gg":
            tradutor = tradutor + "2"

        elif letra in "Hh":
            tradutor = tradutor + "3"

        elif letra in "Ii":
            tradutor = tradutor + "4"

        elif letra in "Jj":
            tradutor = tradutor + "5"

        elif letra in "Kk":
            tradutor = tradutor + "H"

        elif letra in "Ll":
            tradutor = tradutor + "I"

        elif letra in "Mm":
            tradutor = tradutor + "J"

        elif letra in "Nn":
            tradutor = tradutor + "K"

        elif letra in "Oo":
            tradutor = tradutor + "p"

        elif letra in "Pp":
            tradutor = tradutor + "t"

        elif letra in "Qq":
            tradutor = tradutor + "="

        elif letra in "Rr":
            tradutor = tradutor + "+"

        elif letra in "Ss":
            tradutor = tradutor + "-"

        elif letra in "Tt":
            tradutor = tradutor + "_"

        elif letra in "Uu":
            tradutor = tradutor + "f"

        elif letra in "Vv":
            tradutor = tradutor + "{"

        elif letra in "Ww":
            tradutor = tradutor + "["

        elif letra in "Xx":
            tradutor = tradutor + "}"

        elif letra in "Yy":
            tradutor = tradutor + "/"

        elif letra in "Zz":
            tradutor = tradutor + ">"

        else:
            tradutor = tradutor + letra

    return tradutor

print(cripto(input('Digite sua frase: ')))

def descripto(frase):
    tradutor = ""

    for letra in frase:

        if letra in "@":
            tradutor = tradutor + "A"

        elif letra in "#":
            tradutor = tradutor + "B"

        elif letra in "&":
            tradutor = tradutor + "C"

        elif letra in "%":
            tradutor = tradutor + "D"

        elif letra in "$":
            tradutor = tradutor + "E"

        elif letra in "1":
            tradutor = tradutor + "F"

        elif letra in "2":
            tradutor = tradutor + "G"

        elif letra in "3":
            tradutor = tradutor + "H"

        elif letra in "4":
            tradutor = tradutor + "I"

        elif letra in "5":
            tradutor = tradutor + "J"

        elif letra in "H":
            tradutor = tradutor + "K"

        elif letra in "I":
            tradutor = tradutor + "L"

        elif letra in "J":
            tradutor = tradutor + "M"

        elif letra in "K":
            tradutor = tradutor + "N"

        elif letra in "p":
            tradutor = tradutor + "O"

        elif letra in "t":
            tradutor = tradutor + "P"

        elif letra in "=":
            tradutor = tradutor + "Q"

        elif letra in "+":
            tradutor = tradutor + "R"

        elif letra in "-":
            tradutor = tradutor + "S"

        elif letra in "_":
            tradutor = tradutor + "T"

        elif letra in "f":
            tradutor = tradutor + "U"

        elif letra in "{":
            tradutor = tradutor + "V"

        elif letra in "[":
            tradutor = tradutor + "W"

        elif letra in "}":
            tradutor = tradutor + "X"

        elif letra in "/":
            tradutor = tradutor + "Y"

        elif letra in ">":
            tradutor = tradutor + "Z"

        else:
            tradutor = tradutor + letra

    return tradutor

z=1
while z==1:

    SENHA = int(input("DIGITE A SENHA PARA DESCRIPTOGRAFAR: "))

    if SENHA == password:
        print(descripto(input('Digite a frase criptografada: ')))
    else:
        print('SENHA INCORRETA')

    z = int(input("\nDigite 1 para continuar: "))











