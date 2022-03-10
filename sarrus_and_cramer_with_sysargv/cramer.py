#!/bin/python

from sys import argv
import subprocess as sp
import sarrus as sr


def sys22(m, a):
    mx = [
        [ a[0], m[0][1] ],
        [ a[1], m[1][1] ]
    ]
    my = [
        [ m[0][0], a[0] ],
        [ m[1][0], a[1] ]
    ]
    m = [
        [ m[0][0], m[0][1] ],
        [ m[1][0], m[1][1] ]
    ]
    detM = sr.det22(m)

    return [sr.det22(mx) / detM, sr.det22(my) / detM]


def sys33(m, a):
    mx = [
        [ a[0], m[0][1], m[0][2] ],
        [ a[1], m[1][1], m[1][2] ],
        [ a[2], m[2][1], m[2][2] ],
    ]
    my = [
        [ m[0][0], a[0], m[0][2] ],
        [ m[1][0], a[1], m[1][2] ],
        [ m[2][0], a[2], m[2][2] ],
    ]
    mz = [
        [ m[0][0], m[0][1], a[0] ],
        [ m[1][0], m[1][1], a[1] ],
        [ m[2][0], m[2][1], a[2] ],
    ]
    m = [
        [ m[0][0], m[0][1], m[0][2] ],
        [ m[1][0], m[1][1], m[1][2] ],
        [ m[2][0], m[2][1], m[2][2] ],
    ]
    detM = sr.det33(m)

    return [sr.det33(mx) / detM, sr.det33(my) / detM, sr.det33(mz) / detM]


def main():
    llStr = " ".join(map(str, [ e for e in argv if "cramer" not in e]))
    ll = list(llStr.split(" "))
    l = [*ll][0:-1]
    m = [ e.split(",") for e in l ]
    a = list(map(float, [*ll].pop(len(ll) - 1).split(",")))
    for i in range(len(m)):
        m[i] = [ float(e) for e in m[i] ]

    if len(m) == 3 :
        print(sys33(m, a))
    elif len(m) == 2 :
        print(sys22(m, a))
    else :
        print("Ejemplo de uso para sistemas 3x3: ./cramer \"2,5,3 4,1,9 7,0,1\" \"3,0,5\"")
        print("Ejemplo de uso para sistemas 2x2: ./cramer \"2,5 4,1\" \"3,5\"")
        exit(1)


if __name__ == "__main__":
    main()

    # m = 3,1 2,3
    # a = 9,13

    # m = -1,4,3 0,2,2 1,-3,5
    # a = 2,1,0

    # m = 3,2,1 2,0,1 -1,1,2
    # a = 1,2,4
