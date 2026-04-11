from punto import Punto
from math import sqrt, pow

class Segmento:

    def __init__(self, A: Punto, B: Punto):
        self.A = A
        self.B = B

    def lunghezza(self):
        """Metodo che ritorna la lunghezza del segmento con la formula radice di (Bx - Ax)2 + (By - Ay)2""" 
        return sqrt(pow(self.B.x - self.A.x, 2) + pow(self.B.y - self.A.y, 2))

    def __str__(self):
        return f"Il segmento di estremi A{self.A} e B{self.B} ha lunghezza {self.lunghezza():.2f}"
        