#!/bin/python
import argparse


def std_err(msg):
    print(msg)
    cli().print_help()
    exit(1)


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


def treat_m(m):
    try:
        return [ list(map(float, e.split(" ")))  for e in m ]
    except ValueError:
        raise ValueError


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="sarrus",
        description='Programa de CLI para calcular determinanates de matrices 2x2 o 3x3.',
        usage="%(prog)s [OPTIONS] [MATRIX] \nejemplo: 2x2: %(prog)s \"2 -6\" \"12 0\"\nejemplo: 3x3: %(prog)s \"2 -6 8\" \"12 0 1\" \"5 6 3\""
    )

    parser.add_argument(
        "matrix",
        type=str,
        nargs="+",
        help="<Requirido> Matriz para la cual se calculará su determinante",
    )


    return parser


def main():
    args = cli().parse_args()

    try:
        m = treat_m([*args.matrix])

        if len(m) == 3:
            print(det33(m))
        elif len(m) == 2:
            print(det22(m))
        else:
            std_err('La matriz es de un grado no aceptable.')
    except ValueError:
        std_err("ValueError: Los valores de la matriz ingresada no pueden ser procesados.")
    except IndexError:
        std_err("IndexError: Los valores de la matriz ingresada no son congruentes.")


if __name__ == "__main__":
    main()
