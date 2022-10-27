import random
#Implementar FIFO, LRU y CLOCK, comparar su eficiencia, calculando la cantidad de HIT y MISS, asumir tamaños de paginas, largo de la secuencia y la cantidad de memoria
#El ultimo valor de la secuencia no se toma en cuenta

#Definir variables

cantidad_memoria = 128
tamaño_paginas = 4
secuencia = []
tamaño_secuencia = 15
hit = 0
miss = 0
#El tamaño de la secuencia será de 15 caracteres y serán random

#Asignar valores del arrelo

contador = 0
while (contador < tamaño_secuencia):
    secuencia.append(random.randint(1,8))
    contador = contador+1

#print(secuencia, "\n\n")

# FIFO #
print("\n\n################# FIFO #################")


print("### FIFO ###")
orden_cambio_FIFO = [0, 0, 0, 0]
hit_miss = 0 
contador = 0

for i in secuencia:

    print("\n\nSecuencia",secuencia)
    print("\nMemoria",orden_cambio_FIFO)

    #print(orden_cambio_FIFO)
    #print(i)
    for j in orden_cambio_FIFO:
        if (i == j):
            hit_miss = 1
            break
            
    if (hit_miss == 1):
        print("\nHIT", i, "con", j)
        #print(i, "con ", j)
        hit = hit+1
        hit_miss = 0

    elif (hit_miss == 0):
        miss = miss+1
        orden_cambio_FIFO[contador] = i
        contador = contador + 1
        if (contador == 4):
            contador = 0

print("\nHIT con FIFO: ", hit)
print("MISS con FIFO: ",miss)

# LRU #
# Se pensó de la siguiente forma: 
# - Está el arreglo donde se guardan los datos como en FIFO, pero aquí se creó otro arreglo, el cual cumple la función de asignar la prioridad de cambio
#   de cada número; Cuando se "utiliza uno, pasa al final de la prioridad (mayor número), y cuando hay que hacer un reemplazo, se hace con el menor número
#   de orden_prioridad. Se relacionan directamente el arreglo orden_cambio_LRU con orden_cambio, ya que, dependiendo de la dirección de orden_prioridad, 
#   se efectúa el cambio en orden_prioridad_LRU"

print("\n\n################# LRU #################")
orden_cambio_LRU = [0, 0, 0, 0] # Se guarda el cambio de las variables
orden_prioridad = [1, 2, 3, 4] # Se guarda el orden de cambio de las variables
hit_miss = 0 
contador = 5 # Aumenta con los cambios de variables
hit = 0
miss = 0
contadorv2 = 0 # Sirve para guiar donde se realizará el cambio cuando no se encuentre la variable en memoria

for i in secuencia:
    
    print("\n\nSecuencia",secuencia)
    print("\nOrden reemplazo",orden_prioridad)
    print("\nMemoria",orden_cambio_LRU)

    # En caso de que se encuentre la variable en memoria
    for j in orden_cambio_LRU:
        pass
        if (i == j):
            hit_miss = 1
            break

    # En caso de que no se encuentre la variable en memoria
    if (hit_miss == 0):
        #print(i, "con", j)
        miss = miss+1
        #hit_miss = 0
        reemplazo = min(orden_prioridad, key=int)  # Se busca el valor más bajo de orden_prioridad
        #print("reemplazo:", reemplazo, "\n")
        contadorv2 = 0
        
        for h in orden_prioridad: # Se busca la ubicación del elemento más pequeño de orden_prioridad
            if (h == reemplazo):
                #print("\ncontador 2:", contadorv2)
                reemplazo2 = orden_prioridad[contadorv2]
                orden_prioridad[contadorv2] = contador
                contador = contador+1
                #print(orden_prioridad)
                break

            contadorv2 = contadorv2+1
        #print("contadorrrrrrr: ",contadorv2  )
        orden_cambio_LRU[contadorv2] = i # 
        #print(orden_cambio_LRU)

    
    elif (hit_miss == 1):
        hit = hit+1
        hit_miss = 0
        reemplazo = min(orden_prioridad, key=int)
        contadoraux = 0
        #print("\nfuncionaaaaaaa")
        #print("reemplazo:", reemplazo, "\n")

        for a in orden_cambio_LRU:
            if (a == i):
                orden_prioridad[contadoraux] = contador
                contador = contador+1
                #print(orden_prioridad)
                break
            contadoraux = contadoraux+1
            
        print("\nHIT:", i, "con", j)
    #print("FUNCIONAAAAAAAAAAAAAAAAAAAAAAAAAAa")
    
print("\nHIT con LRU: ", hit)
print("MISS con LRU: ",miss)


# CLOCK #

# Asignar un bit de modificado y un puntero (el cual comienza en la primera pagina); Cuando un número entra a una pagina, su bit de modificado es 1, pero cuando se necesita realizar un cambio, 
# el puntero se mueve en forma ascendente (por la memoria), buscando una pagina, cuyo bit de modificado sea 0, en el caso de que el puntero intente acceder a una pagina, cuyo bit de modiificado
# sea 1, este se vuelve 0 y pasa a la siguiente página. Gracias a esto, se le da una segunda oportunidad a la pagina que tenga un bit de modificado = 1.

print("\n\n################# CLOCK #################")


print("HIT con CLOCK: ", hit)
print("MISS con CLOCK: ",miss)