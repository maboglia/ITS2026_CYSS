from punto import Punto
from segmento import Segmento
import math

class Triangolo:

    def __init__(self, A: Punto, B: Punto, C: Punto):
        self.A = A
        self.B = B
        self.C = C

        self.AB = Segmento(A, B)
        self.AC = Segmento(A, C)
        self.BC = Segmento(B, C)

    def perimetro(self):
        return self.AB.lunghezza() + self.AC.lunghezza() + self.BC.lunghezza()
    
    def area(self):
        """Applico la formula di Erone per il calcolo della superficie dato il semi-perimetro"""
        sp = self.perimetro() / 2

        return math.sqrt(sp * (sp - self.AB.lunghezza()) * (sp - self.AC.lunghezza()) * (sp - self.BC.lunghezza()))

    def __str__(self):
        return f"Questo Triangolo ha un perimetro di {self.perimetro():.2f} e ha una superficie di {self.area():.2f}"