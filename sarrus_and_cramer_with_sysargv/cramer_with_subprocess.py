#!/bin/python

from sys import argv
import subprocess as sp


def det(m):
    return float(
        sp.check_output("./sarrus.py {}".format(m), shell=True).__str__()[2:-3]
    )


def sys22(m, a):
    mx = "{},{} {},{}".format(a[0], m[0][1], a[1], m[1][1])
    my = "{},{} {},{}".format(m[0][0], a[0], m[1][0], a[1])
    m = "{},{} {},{}".format(m[0][0], m[0][1], m[1][0], m[1][1])
    detM = det(m)

    return [det(mx) / detM, det(my) / detM]


def sys33(m, a):
    mx = "{},{},{} {},{},{} {},{},{}".format(
        a[0], m[0][1], m[0][2],
        a[1], m[1][1], m[1][2],
        a[2], m[2][1], m[2][2],
    )
    my = "{},{},{} {},{},{} {},{},{}".format(
        m[0][0], a[0], m[0][2],
        m[1][0], a[1], m[1][2],
        m[2][0], a[2], m[2][2],
    )
    mz = "{},{},{} {},{},{} {},{},{}".format(
        m[0][0], m[0][1], a[0],
        m[1][0], m[1][1], a[1],
        m[2][0], m[2][1], a[2],
    )
    m = "{},{},{} {},{},{} {},{},{}".format(
        m[0][0], m[0][1], m[0][2],
        m[1][0], m[1][1], m[1][2],
        m[2][0], m[2][1], m[2][2],
    )
    detM = det(m)

    return [det(mx) / detM, det(my) / detM, det(mz) / detM]


def main():
    llStr = " ".join(map(str, [ e for e in argv if "cramer" not in e]))
    ll = list(llStr.split(" "))
    l = [*ll][0:-1]
    m = [ e.split(",") for e in l ]
    a = [*ll].pop(len(ll) - 1).split(",")

    if len(m) == 3 :
        print(sys33(m, a))
    elif len(m) == 2 :
        print(sys22(m, a))
    else :
        exit(1)


if __name__ == "__main__":
    main()

    # m = [
    #     [3, 1],
    #     [2, 3],
    # ]

    # a = [9, 13]

    # m = [
    #     [-1,4,3],
    #     [0,2,2],
    #     [1,-3,5],
    # ]

    # a = [2,1,0]

    # m = [
    #     [3,2,1],
    #     [2,0,1],
    #     [-1,1,2],
    # ]

    # a = [1,2,4]
