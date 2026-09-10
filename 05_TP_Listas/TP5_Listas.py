#EJERCICIO 1

notas = [4,5,3,7,9,10,4,5,3,6]
suma = 0
minimo = notas[0]
maximo = notas[0]
for i in range(len(notas)):
    suma = suma + notas[i]
    if notas[i] < minimo:
        minimo = notas[i]
    if notas[i] > maximo:
        maximo = notas[i]
promedio = suma / len(notas)
print(f"""El promedio fue {promedio}
La nota mas alta {maximo}
La nota mas baja {minimo}""")

#EJERCICIO 2

lista_prod = list()
for i in range(1,6):
    pedir_prod = input(f"Ingrese el producto {i}: ")
    while pedir_prod.isdigit():
        pedir_prod = input("No se permite solo digitos.Intente otra vez: ")
    lista_prod.append(pedir_prod)
    lista_ordenada = sorted(lista_prod)
    print(lista_ordenada)
    quitar_prod = input("Seleccione el producto a eliminar: ")
    if quitar_prod in lista_ordenada:
        lista_ordenada.remove(quitar_prod)
    print(lista_ordenada)

#EJERCICIO 3

import random
lista_R = random.sample(range(1,101), 15)
lista_par = list()
lista_impar = list()
for i in range(len(lista_R)):
    if lista_R[i] % 2 == 0:
        lista_par.append(lista_R[i])
    else:
        lista_impar.append(lista_R[i])
print(f"""Lista par: {lista_par} 
Lista impar: {lista_impar}""")

#EJERCICIO 4 

datos = [1,3,5,3,7,1,9,5,1]
NDatos = list()
for i in range(len(datos)):
    if (datos[i] not in NDatos):
        NDatos.append(datos[i])
print(NDatos)