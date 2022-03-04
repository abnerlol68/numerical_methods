import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
from tabulate import tabulate as tab


# Función a evaluar
def f(x):
    return Decimal((x ** 4) + (3 * x ** 3) - 2)


# Grafico
def graphic(x, y):
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.plot(x,y)
    plt.grid()
    plt.title('x^4+3x^3-2')
    plt.show()


# Error relativo
def err(x_r, x_a):
    return abs((x_r - x_a) / x_r) * 100


# Falsa posición
def x_r(x_i, x_u):
    return Decimal(x_u - (f(x_u) * (x_i - x_u) / (f(x_i) - f(x_u))))


def tb_false_position(x_i, x_u):
    # Numéro de iteraciones
    i = 1
    # Error porcentual con valor exorbitante inicial
    err_p = 999
    table = []

    xr = x_r(x_i,x_u)
    xr_a = xr

    fx_i = f(x_i)
    fx_u = f(x_u)
    fx_r = f(xr)
    fx_i_fx_u = fx_i * fx_r

    fmt = '{0:.9g}'
    head = [
        'Iteracion', 'x_i', 'x_u', 'x_r', 
        'fx_i', 'fx_u', 'fx_r', 'fx_i_fx_u', 'EP'
    ]
    table.append([
        i,
        fmt.format(x_i),
        fmt.format(x_u),
        fmt.format(xr),
        fmt.format(fx_i),
        fmt.format(fx_u),
        fmt.format(fx_r),
        fmt.format(fx_i_fx_u),
        ''
    ])
    
    while err_p > 0.000_1:
        if fx_i_fx_u > 0:
            x_i = xr
            fx_i = f(x_i)
        elif fx_i_fx_u < 0:
            x_u = xr
            fx_u = f(x_u)
        else:
            break

        i += 1
        xr = x_r(x_i,x_u)
        fx_r = f(xr)
        fx_i_fx_u = fx_i * fx_r
        err_p = err(xr,xr_a)
        xr_a = xr

        table.append([
            i,
            fmt.format(x_i),
            fmt.format(x_u),
            fmt.format(xr),
            fmt.format(fx_i),
            fmt.format(fx_u),
            fmt.format(fx_r),
            fmt.format(fx_i_fx_u),
            '{0:.9g}%'.format(err_p)
        ])

    return tab(table, headers=head)


def main():
    # Valores de acotación
    x_i = 0
    x_u = 1

    print(tb_false_position(x_i, x_u))

    # Graficación inicial
    x = np.linspace(-2,2,30)
    y = list(map(f, x))
    graphic(x,y)

if __name__ == "__main__":
    main()
