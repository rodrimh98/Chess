# -*- coding: utf-8 -*-

import numpy as np

#Crea el tablero
class square (object):
    pos_i = 0
    pos_j = 0
    color = None
    influencia = None
    pieza = None
    value = None

T = np.empty((8,8),dtype= object)

def table ():

    for i in range (8):             #
        for j in range(8):          #cf
            T[i,j] = square()     # Crea el array de tablero asignando a cada espacion el objeto cuadrado
            T[i,j].pos_i = i        #  y sus correspondientes coordenadas de 0 a 7
            T[i,j].pos_j = j        #

            if (((T[i,j].pos_i+T[i,j].pos_j)%2) == 0):  #
                T[i,j].color = 'black'                  #Establece el color de la casilla segun la posicion
            else:                                       #
                T[i,j].color = 'white'                  #

    T[3,4].value = T[3,3].value = T[4,3].value = T[4,4].value = 4 # Establece el valor de las casillas centrales
    


    for j in range(2,6):
        for i in range(2,6):
            if T[i,j].value == None:
                T[i,j].value = 3

    for i in range(1,7):
        for j in range(1,7):
            if T[i,j].value == None:
                T[i,j].value = 2
    
    for i in range (8):
        for j in range(8):
            if T[i,j].value == None:
                T[i,j].value = 1

    return T

#Fin de creacion del tablero