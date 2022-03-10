#!/bin/python

import argparse
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


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cramer",
        description='Programa de CLI para resolver sistemas de ecuaciones de 2x2 o 3x3.',
        usage=
"""%(prog)s [OPTIONS] [-m] [MATRIX] [a] [VECTOR] 
ejemplo: 2x2: %(prog)s -m \"2 -6\" \"12 0\" -a \"3 9\"
ejemplo: 3x3: %(prog)s -m \"2 -6 8\" \"12 0 1\" \"5 6 3\" -a \"2 0 1\""""
    )

    parser.add_argument(
        "-m", "--matrix",
        type=str,
        nargs="+",
        help="<Requirido> Matriz de coeficientes del sistema de ecuaciones.",
    )

    parser.add_argument(
        "-a", "--independent-terms",
        type=str,
        nargs="+",
        help="<Requirido> Vector de los términos independientes.",
    )


    return parser


def main():
    args = cli().parse_args()

    try:
        m = sr.treat_m([*args.matrix])
        a = sr.treat_m([*args.independent_terms])[0]

        if len(m) == 3 and len(a) == 3:
            print(sys33(m, a))
        elif len(m) == 2 and len(a) == 2:
            print(sys22(m, a))
        else:
            sr.std_err('La matriz o del vector de términos independientes es de un grado no aceptable.')
    except ValueError:
        sr.std_err("ValueError: Los valores de la matriz o del vector de términos independientes ingresada no pueden ser procesados.")
    except IndexError:
        sr.std_err("IndexError: Los valores de la matriz o del vector de términos independientes ingresada no son congruentes.")


if __name__ == "__main__":
    main()
