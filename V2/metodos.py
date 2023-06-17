import math
import numpy as np
import sympy as sp


# Definir las variables simbólicas
x_sym = sp.Symbol('x')
y_sym = sp.Symbol('y')
def f(expresion, x):
    return eval(expresion)

def biseccion(func_txt, x_i, x_u,tol=0.0004,max_step = 10):
    """
    Encuentra la raíz de la función f en el intervalo [x_i,x_u]
    usando el método de bisección con una tolerancia dada.
    """
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(func_txt)

    # Convertir la función a funcion numérica
    f = sp.lambdify(x_sym, f_expr)
    tabla = []
    conteo=0
    ea=1
    #Paso 1
    if f(x_i) * f(x_u) > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")
    
    while ea > tol: #criterio de paro
        #Paso 2
        raiz = (x_i + x_u) / 2 #aproximacion de la raiz
        ea=abs((x_u-x_i)/2)
        conteo+=1
        fa = f(x_i)
        fb = f(x_u)
        fc = f(raiz)
        tabla.append([conteo,x_i,x_u,raiz,ea])
        # print(f"{conteo}\t{x_i:.4f}\t{x_u:.4f}\t{raiz:.4f}\t{f(raiz):.2f}\t{ea:.4f}")
        #Paso 3
        if fa*fc == 0: #c)
            return tabla
        elif fa * fc < 0: #a)
            x_u = raiz
        elif fa * fc > 0: #b)
            x_i = raiz
        if conteo>max_step:
            break
    return tabla

def punto_fijo(func_txt, x0, tolerance, max_iterations):
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(func_txt)

    # Convertir la función a funcion numérica
    f = sp.lambdify(x_sym, f_expr)
    x = x0
    iterations = 1
    error = np.inf
    
    table = []
    
    while error > tolerance and iterations <= max_iterations:
        x_new = f(x)
        error = np.abs(x_new - x)
        
        table.append([iterations, x, round(error,8), round(f(x),9), x_new])
        
        x = x_new
        iterations += 1
    
    return table
def falsa_posicion(funcion, a, b, tolerancia, iteraciones_max):
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(funcion)
    # Convertir la función a funcion numérica
    f_num = sp.lambdify(x_sym, f_expr)
    
    tabla_iteraciones = []
    
    # Calcular los valores iniciales de la función
    f_a = f_num(a)
    f_b = f_num(b)
    
    # Verificar que el intervalo contiene una raíz
    if f_a * f_b >= 0:
        print("El intervalo no contiene una raíz.")
        return tabla_iteraciones
    
    # Inicializar variables
    iteracion = 0
    error = float('inf')
    
    while error > tolerancia and iteracion < iteraciones_max:
        iteracion += 1
        
        # Calcular el nuevo punto
        x_nuevo = (a*f_b - b*f_a) / (f_b - f_a)
        
        # Calcular el valor de la función en el nuevo punto
        f_x_nuevo = f_num(x_nuevo)
        
        # Calcular el error relativo
        if x_nuevo != 0:
            error = abs((f_num(x_nuevo)))
        
        # Actualizar los valores
        if f_a * f_x_nuevo < 0:
            b = x_nuevo
            f_b = f_x_nuevo
        else:
            a = x_nuevo
            f_a = f_x_nuevo
        
        # Agregar los valores a la tabla de iteraciones
        tabla_iteraciones.append((iteracion, x_nuevo, f_x_nuevo, error))
    
    return tabla_iteraciones

def secante_method(func_txt, x0, x1, tolerance, max_iterations):
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(func_txt)

    # Convertir la función a funcion numérica
    f = sp.lambdify(x_sym, f_expr)
    x = [x0, x1]
    iterations = 1
    error = np.inf
    
    table = []
    
    while error > tolerance and iterations <= max_iterations:
        fx0 = f(x[0])
        fx1 = f(x[1])
        
        x_new = x[1] - (fx1 * (x[1] - x[0])) / (fx1 - fx0)
        error = np.abs(x_new - x[1])
        
        table.append([iterations, x[1], round(f(x[1]),8),round(error,8)])
        
        x[0] = x[1]
        x[1] = x_new
        iterations += 1
    
    return table
def euler_method(f, x0, y0, h, num_iterations):
    x = x0
    y = y0
    
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(f)
    
    # Convertir la función a una función numérica
    f_num = sp.lambdify((x_sym, y_sym), f_expr)
    
    table = []
    
    for i in range(1,num_iterations+1):
        table.append([i, x, y, f_num(x, y), y + h * f_num(x, y)])
        
        y_new = y + h * f_num(x, y)
        x += h
        y = y_new
    
    return table

def newton_raphson(f, x0, tolerance, max_iterations):
    x = x0
    iterations = 1
    error = np.inf
    
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(f)
    
    # Calcular la derivada
    f_prime = sp.diff(f_expr, x_sym)
    
    # Convertir la función y la derivada a funciones numéricas
    f_num = sp.lambdify(x_sym, f_expr)
    f_prime_num = sp.lambdify(x_sym, f_prime)
    
    table = []
    
    while error > tolerance and iterations < max_iterations:
        fx = f_num(x)
        fpx = f_prime_num(x)
        x_new = x - fx / fpx
        error = np.abs(x_new - x)
        table.append([iterations, x, error, fx])
        x = x_new
        iterations += 1
    
    return table


