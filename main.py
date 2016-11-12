# -*- coding: utf-8 -*-


from tkinter import *
import table as tab
import piezas as p

#master = Tk()

#w = Canvas(master, width=700, height = 700)

#w.pack()
#w.create_line(((50,50),(50,650)),((50,650),(650,650)),(650,650),(650,50),(650,50),(50,50))

#Crea el tablero
T = tab.table()
p1 = p.peon()
p1.pos=[1,0]

#for i in range (8):             #
#    for j in range(8):          #cf
#        w.create_rectangle(50+T[i,j].pos_i*75, 650-T[i,j].pos_j*75,
#                           50+(T[i,j].pos_i + 1)*75, 650-(T[i,j].pos_j+1)*75,
#                           fill=T[i,j].color) # Crea la cuadricula, el signo - despues de 650 es para que vayan de abajo a arriba
print (p1.pos)
p1.influence()
print (p1.influence_pos)
p1.posible_move()

print (p1.pos)
p1.influence()
print (p1.influence_pos)

#Fin de creacion del tablero