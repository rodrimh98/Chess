# -*- coding: utf-8 -*-
import pdb

from tkinter import *
import table as tab
import piezas as peon

#master = Tk()

#w = Canvas(master, width=700, height = 700)

#w.pack()
#w.create_line(((50,50),(50,650)),((50,650),(650,650)),(650,650),(650,50),(650,50),(50,50))

#Crea el tablero
T = tab.table()


#
#for i in range (8):             #
#    for j in range(8):          #cf
#        w.create_rectangle(50+T[i,j].pos_i*75, 650-T[i,j].pos_j*75,
#                           50+(T[i,j].pos_i + 1)*75, 650-(T[i,j].pos_j+1)*75,
#                           fill=T[i,j].color) # Crea la cuadricula, el signo - despues de 650 es para que vayan de abajo a arriba


#Colocacion de todos lpos peones en la fila 2
p = []
for i in range(8):
	p.append(peon.peon())
	p[i].name = 'p' + str(i)
	p[i].pos  = [1,i]

	T[p[i].pos[0],p[i].pos[1]].pieza = p[i].name 	
#
#
#Prueba de algoritmo con peones
score = []
temp_score = []
max_score = [0,0]

pdb.set_trace()

for a in range(8):
	p[a].posible_move()
	p[a].temp_influence()
	p[a].score()
	if p[a].score > max_score:
		max_score = p[a].temp_pos

print (max_score)

#Fin de creacion del tablero