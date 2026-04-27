

class Mammifero:

    def __init__(self):
        print("Mammifero costruito")


class Tigre(Mammifero):

    def __init__(self, nome):
        super().__init__()
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome


m1 = Mammifero()

t1 = Tigre("jenny")

print(t1.nome)

t1.nome = "gianna"
print(t1.nome)