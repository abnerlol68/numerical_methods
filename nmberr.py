#!/bin/python

from sys import argv

def half_value(values):
    sum = 0
    for val in values:
        sum += float(val)
    return sum / len(values)


def errors(values):
    half = half_value(values)
    table = "Err_abs\t\t\tErr_rel\t\t\tErr_por"

    print("Half: {}".format(half))

    for val in values:
        err_abs = abs(float(val) - half)
        err_rel = err_abs / half
        err_por = "{:.3f}%".format(err_rel * 100)
        table += "\n{:.3f}\t\t\t{:.3f}\t\t\t{}".format(err_abs, err_rel, err_por)

    return table


def print_err():
    print("Error, use of the program: ./nmberr.py [...values]")
    exit(1)


def main():
    if len(argv) < 2:
        print_err()
    for arg in argv:
        if arg == argv[0]:
            continue
        if isinstance(arg, int) and isinstance(arg, float):
            print_err()

    head, *tail = argv
    print(errors(tail))


if __name__ == "__main__":
    main()