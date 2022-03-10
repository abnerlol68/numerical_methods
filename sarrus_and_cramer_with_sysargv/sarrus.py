#!/bin/python

from sys import argv


def det33(m):
    return (
        m[0][0] * m[1][1] * m[2][2] +
        m[1][0] * m[2][1] * m[0][2] +
        m[2][0] * m[0][1] * m[1][2] -
        m[0][2] * m[1][1] * m[2][0] -
        m[1][2] * m[2][1] * m[0][0] -
        m[2][2] * m[0][1] * m[1][0]
    )


def det22(m):
    return m[0][0] * m[1][1] - m[1][0] * m[0][1]


def main():
    # Se agrega un elemento de argv si contiene "sarrus" este se excluye
    lStr = " ".join(map(str, [ e for e in argv if "sarrus" not in e]))
    # Al str se pasa a lista y se pera por los espacios
    l = list(lStr.split(" "))
    # Se agrega un elemento dividido por "," en cada elemento de l
    m = [ e.split(",") for e in l ]
    # Parceo de string a float por cada elemento de la matriz
    for i in range(len(m)):
        m[i] = [ float(e) for e in m[i] ]

    if len(m) == 3 :
        print(det33(m))
    elif len(m) == 2 :
        print(det22(m))
    else :
        exit(1)


if __name__ == "__main__":
    main()


# "3,2 5,6"
# "0,2,1 3,-1,5 6,9,8"
