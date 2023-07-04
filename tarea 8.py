'''
1 - Pedir un numero, sacar el factorial y mostrar el resultado. Ejemplo: el factorial de 8
seria 8*7*6*5*4*3*2*1 = 1*2*3*4*5*6*7*8 = 40320.'''
# Pedimos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Inicializamos el factorial como 1
factorial = 1

# Calculamos el factorial multiplicando el número por todos los números menores a él hasta llegar a 1
while numero > 0:
    factorial *= numero
    numero -= 1

# Mostramos el resultado
print("El factorial es:", factorial)


'''2 - usando el ciclo while, pedir 5 valores enteros, sumarlos y mostrar la suma y el
promedio, recordar que el promedio es la suma de todos los numeros dividido la cantidad.'''
# Inicializamos la suma y el contador en 0
suma = 0
contador = 0

# Pedimos al usuario que ingrese 5 valores enteros
while contador < 5:
    valor = int(input("Ingrese un valor entero: "))
    suma += valor
    contador += 1

# Calculamos el promedio dividiendo la suma entre la cantidad de valores ingresados
promedio = suma / 5

# Mostramos la suma y el promedio
print("La suma es:", suma)
print("El promedio es:", promedio)


'''3 - Usando un ciclo de repeticion y un match dentro del ciclo de repeticion, pedir numeros
y decir si es par o impar, sale del ciclo cuando se ingresa 0.'''
# Pedimos al usuario que ingrese números hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número (ingrese 0 para salir): "))

    # Salimos del ciclo si el número ingresado es 0
    if numero == 0:
        break

    # Verificamos si el número es par o impar y mostramos el resultado
    if numero % 2 == 0:
        print(numero, "es par.")
    else:
        print(numero, "es impar.")


'''4 - Pedir 10 valores aleatorios e imprimir lo siguiente:

* Cuantos valores son pares y cuantos impares.

* Cuantos valores son multiplo de 5 y de 3 al mismo tiempo.

* la suma total de los valores

* Cuantos valores son negativos y multiplo de 2.

*Promedio total.'''
# Importamos el módulo random para generar números aleatorios
import random

# Inicializamos las variables contadoras y la suma total
pares = 0
impares = 0
multiplos_5_y_3 = 0
suma_total = 0
negativos_multiplo_2 = 0

# Pedimos al usuario que ingrese 10 valores aleatorios
for _ in range(10):
    valor = random.randint(-100, 100)  # Generamos un número aleatorio entre -100 y 100

    # Verificamos si el valor es par o impar y actualizamos las variables contadoras
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Verificamos si el valor es múltiplo de 5 y de 3 al mismo tiempo
    if valor % 5 == 0 and valor % 3 == 0:
        multiplos_5_y_3 += 1

    # Actualizamos la suma total de los valores
    suma_total += valor

    # Verificamos si el valor es negativo y múltiplo de 2
    if valor < 0 and valor % 2 == 0:
        negativos_multiplo_2 += 1

# Calculamos el promedio total dividiendo la suma total entre 10
promedio_total = suma_total / 10

# Mostramos los resultados obtenidos
print("Cantidad de valores pares:", pares)
print("Cantidad de valores impares:", impares)
print("Cantidad de valores múltiplos de 5 y de 3:", multiplos_5_y_3)
print("Suma total de los valores:", suma_total)
print("Cantidad de valores negativos y múltiplos de 2:", negativos_multiplo_2)
print("Promedio total:", promedio_total)
