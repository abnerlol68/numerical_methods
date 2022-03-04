#!/bin/python

from sys import argv


def det33(m):
    return (
        float(m[0][0]) * float(m[1][1]) * float(m[2][2]) +
        float(m[1][0]) * float(m[2][1]) * float(m[0][2]) +
        float(m[2][0]) * float(m[0][1]) * float(m[1][2]) -
        float(m[0][2]) * float(m[1][1]) * float(m[2][0]) -
        float(m[1][2]) * float(m[2][1]) * float(m[0][0]) -
        float(m[2][2]) * float(m[0][1]) * float(m[1][0])
    )


def det22(m):
    return float(m[0][0]) * float(m[1][1]) - float(m[1][0]) * float(m[0][1])


def main():
    # Se agrega un elemento de argv si no contiene "sarrus"
    lStr = " ".join(map(str, [ e for e in argv if "sarrus" not in e]))
    # Al str se pasa a lista y se pera por los espacios
    l = list(lStr.split(" "))
    # Se agrega un elemento dividido por "," en cada elemento de l
    m = [ e.split(",") for e in l ]

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
