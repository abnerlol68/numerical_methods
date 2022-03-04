# Modulos de la librería de Python que nos ayudarán
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
from sympy import Symbol, diff
from tabulate import tabulate as tab

### Declaración de atributos

# Declara el símbolo que se va 
# a usar como variable en la ecuación
x = Symbol('x')
# Declaramos la ecuación
g = (x ** 4) + (3 * x ** 3) - 2
# Obtenemos la derivada de la ecuación 
# con el método diff() que se encuentra en el módulo scipy.misc
gd = diff(g, x)
# Obtenemos la segunda derivada de la 
# ecuación con el método diff() que se encuentra en el módulo scipy.misc
gd2 = diff(gd, x)
# Declaramos el nivel de tolerancia, este 
# se tomara como porcentaje es decir 0.1 en la variable será el 0.1%
tol = 0
# Definimos la cabecera de nuestra tabla
head = ['Iteracion', 'x_i', 'x_r', 'fx_i', "f'x_i", 'EP']


# Función a evaluar
def f(z):
    return Decimal((z ** 4) + (3 * z ** 3) - 2)


# Grafico
def graphic(x, y):
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.plot(x,y)
    plt.grid()
    plt.title('x^4+3x^3-2')
    plt.show()


# Error relativo
def err(x_n, x_a):
    return abs((x_n - x_a) / x_n) * 100
    

# Newton Rapson ecuación
def x_r(x_i):
    solve = x_i - (g.subs(x, x_i) / gd.subs(x, x_i))
    return round(solve, 8)


# Líneas de código repetitivas
def __getvalues(x_i, table, i):
    # Obtenemos el nuevo valor de x
    xr = x_r(x_i)
    # Obtenemos el valor de Y ó f(x) ó función con respecto de X
    fx_i = round(g.subs(x, x_i), 8)
    # Obtenemos el valor de la derivada de la función
    fdx_i = round(gd.subs(x, x_i), 8)
    # Obtenemos el valor relativo porcentual inicial
    err_p = err(xr, x_i)

    fmt = '{0:.9g}'
    table.append([
        i,
        str(x_i),
        str(xr),
        str(fx_i),
        str(fdx_i),
        str(err_p)
    ])

    return err_p, xr


# Revisa que el método pueda converger o no
def __check(x_i):
    response = (g.subs(x, x_i) * gd2.subs(x, x_i)) / (gd.subs(x, x_i) ** 2)
    return abs(response) < 1


def mt_newton(x_i):
    if __check(x_i):
        # Numéro de iteración
        i = 1
        # Definimos un array para la tabla
        table = []
        if gd.subs(x, x_i) != 0:
            values = __getvalues(x_i, table, i)
            err_p, x_i = values[0], values[1]
        else:
            return "El método no puede ser aplicado"

        while err_p > tol:
            values = __getvalues(x_i, table, i)
            err_p, x_i = values[0], values[1]
            i += 1

        return tab(table, headers=head)
    else:
        return "El método no puede converger"


## Método Main ##
def main():
  print(mt_newton(5))
  
  # Graficacion inicial
  coorX = np.linspace(-2, 2, 30)
  coorY = list(map(f, coorX))
  graphic(coorX, coorY)


if __name__ == '__main__':
  main()
