import random
#Implementar FIFO, LRU y CLOCK, comparar su eficiencia, calculando la cantidad de HIT y MISS, asumir tamaños de paginas, largo de la secuencia y la cantidad de memoria
#El ultimo valor de la secuencia no se toma en cuenta

# Cada proceso ocupa 1 mega de espacio. Por cada miss se descuenta 1 mega

#Definir variables

tamaño_paginas = 4 # No es modificable
secuencia = []
tamaño_secuencia = 15 # El tamaño de la secuencia puede ser variable, pero por defecto se dejará en 15
memoria_total = 16 # Se representa en MB de memoria

contador = 0
while (contador < tamaño_secuencia): # Se le asignan valores random a la secuencia
    secuencia.append(random.randint(1,8))
    contador = contador+1


# FIFO #
print("\n\n################# FIFO #################")

orden_cambio_FIFO = [0, 0, 0, 0] # Páginas en las que se trabajará
hit_miss = 0 # Sirve para ver si hay HIT o MISS
contador = 0 
hit_FIFO = 0
miss_FIFO = 0
mostrar_hit = 0
memoria_FIFO = memoria_total

for i in secuencia:

    print("\n\nSecuencia",secuencia)
    print("\nMemoria",orden_cambio_FIFO)
    if (mostrar_hit == 1):
        print("\nHIT:", j, "con", j)
        mostrar_hit = 0

    for j in orden_cambio_FIFO: # En caso de que se encuentre la variable i de la secuencia en memoria
        if (i == j):
            hit_miss = 1
            break
            
    if (hit_miss == 1): # Simplemente se le suma +1 a HIT y pasa al siguiente valor del arreglo
        #print("\nHIT", i, "con", j)
        hit_FIFO = hit_FIFO+1
        hit_miss = 0
        mostrar_hit = 1

    elif (hit_miss == 0): # Se le suma +1 a MISS y procede a hacer el reemplazo correspondiente en la pagina que toca, la cual es representada por "contador"
        miss_FIFO = miss_FIFO+1
        orden_cambio_FIFO[contador] = i
        contador = contador + 1
        if (contador == 4):
            contador = 0
        memoria_FIFO = memoria_FIFO-1

    if (memoria_FIFO == 0):
        print("\n###### Error en FIFO, falta Memoria ######")
        break

print("\nHIT con FIFO: ", hit_FIFO)
print("MISS con FIFO: ",miss_FIFO)
print("Total de memoria al final de FIFO =", memoria_FIFO)

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
hit_LRU = 0
miss_LRU = 0
contadorv2 = 0 # Sirve para guiar donde se realizará el cambio cuando no se encuentre la variable en memoria
mostrar_hit = 0
memoria_LRU = memoria_total

for i in secuencia:
    
    print("\n\nSecuencia",secuencia)
    print("\nOrden reemplazo",orden_prioridad)
    print("\nMemoria",orden_cambio_LRU)
    if (mostrar_hit == 1):
        print("\nHIT:", j, "con", j)
        mostrar_hit = 0

    # En caso de que se encuentre la variable en memoria
    for j in orden_cambio_LRU:
        pass
        if (i == j):
            hit_miss = 1
            break

    # En caso de que no se encuentre la variable en memoria
    if (hit_miss == 0):
        miss_LRU = miss_LRU+1
        reemplazo = min(orden_prioridad, key=int)  # Se busca el valor más bajo de orden_prioridad
        contadorv2 = 0
        
        for h in orden_prioridad: # Se busca la ubicación del elemento más pequeño de orden_prioridad
            if (h == reemplazo):
                reemplazo2 = orden_prioridad[contadorv2]
                orden_prioridad[contadorv2] = contador
                contador = contador+1
                break

            contadorv2 = contadorv2+1
        orden_cambio_LRU[contadorv2] = i
        memoria_LRU = memoria_LRU-1
    
    elif (hit_miss == 1): # Se encuentra la variable en memoria
        hit_LRU = hit_LRU+1
        hit_miss = 0
        reemplazo = min(orden_prioridad, key=int)
        contadoraux = 0

        for a in orden_cambio_LRU: # Se le asigna el valor 1 la ubicación de orden_prioridad dependiendo de la ubicación donde se hizo HIT en orden_cambio_LRU
            if (a == i):
                orden_prioridad[contadoraux] = contador
                contador = contador+1
                mostrar_hit = 1
                break
            contadoraux = contadoraux+1
            
    if (memoria_LRU == 0):
        print("\n###### Error en LRU, falta Memoria ######")
        break

print("\nHIT con LRU: ", hit_LRU)
print("MISS con LRU: ",miss_LRU)
print("Total de memoria al final de LRU =", memoria_LRU)


# CLOCK #

# Asignar un bit de modificado y un puntero (el cual comienza en la primera pagina); Cuando un número entra a una pagina, su bit de modificado es 1, pero cuando se necesita realizar un cambio, 
# el puntero se mueve en forma ascendente (por la memoria), buscando una pagina, cuyo bit de modificado sea 0, en el caso de que el puntero intente acceder a una pagina, cuyo bit de modiificado
# sea 1, este se vuelve 0 y pasa a la siguiente página. Gracias a esto, se le da una segunda oportunidad a la pagina que tenga un bit de modificado = 1.

print("\n\n################# CLOCK #################")

bit_modificado = [0, 0, 0, 0] # Se utiliza prar llevar un orden del reemplazo
orden_cambio_CLOCK = [0, 0, 0, 0]
hit_miss = 0 
puntero = 0 # Es como un contador 
hit_CLOCK = 0
miss_CLOCK = 0
mostrar_hit = 0
memoria_CLOCK = memoria_total

for i in secuencia:

    print("\n\nSecuencia", secuencia)
    print("\nMemoria", orden_cambio_CLOCK)
    print("\nBit de modificado", bit_modificado)

    if (mostrar_hit == 1):
        print("\nHIT:", j, "con", j)
        mostrar_hit = 0
    
    for j in orden_cambio_CLOCK:
        if (i == j):
            hit_miss = 1
            break
            
    if (hit_miss == 1):
        hit_CLOCK = hit_CLOCK+1
        hit_miss = 0
        mostrar_hit = 1
        buscar_ubicacion_reemplazo1 = 0
        for h in orden_cambio_CLOCK: # Cuando se realiza un HIT, se asigna un 1 en la ubicación donde se realizó un HIT, para así, darle una segunda oportunidad
            if (h == i):
                bit_modificado[buscar_ubicacion_reemplazo1] = 1
                break
            buscar_ubicacion_reemplazo1 = buscar_ubicacion_reemplazo1 +1

    elif (hit_miss == 0):
        miss_CLOCK = miss_CLOCK+1
        validar = True
        while (validar == True): # Al momento de intentar realizar un reemplazo, se busca una ubicación que tenga su bit de modificado = 0 para poder realizar el reemplazo

            if (bit_modificado[puntero] == 0):
                orden_cambio_CLOCK[puntero] = i
                bit_modificado[puntero] = 1
                validar = False
            else: # En el caso de que el bit de modificado al que apunte el puntero sea 1, se deja en 0 y se pasa a la siguiente página
                bit_modificado[puntero] = 0
                puntero = puntero+1
                if (puntero == 4):
                    puntero = 0

        puntero = puntero + 1
        if (puntero == 4):
            puntero = 0
        memoria_CLOCK = memoria_CLOCK-1

    if (memoria_CLOCK == 0):
        print("\n###### Error en CLOCK, falta Memoria ######")
        break

print("\nHIT con CLOCK: ", hit_CLOCK)
print("MISS con CLOCK: ",miss_CLOCK)
print("Total de memoria al final de CLOCK =", memoria_CLOCK)

###### Mostrar resultador finales ######
print ("\n\n\n######## Conclusiones ########")

print("\n##FIFO##\nHIT:", hit_FIFO, "\nMISS:", miss_FIFO, "\nMemoria Total:", memoria_FIFO)
print("\n##LRU:##\nHIT", hit_LRU, "\nMISS:", miss_LRU, "\nMemoria Total:", memoria_LRU)
print("\n##CLOCK##\nHIT", hit_CLOCK, "\nMISS:", miss_CLOCK, "\nMemoria Total:", memoria_CLOCK)
