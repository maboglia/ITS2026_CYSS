from punto import Punto
from segmento import Segmento
from triangolo import Triangolo

A = Punto(2, 2)
B = Punto(6, 2)
C = Punto(2, 5)

AB = Segmento(A, B)
BC = Segmento(B, C)
AC = Segmento(A, C)

triangolo = Triangolo(A,B,C)

print(triangolo)
