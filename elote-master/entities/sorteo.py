import random
class Sorteo:
    def _init_(self, n1, n2, n3):
        self.numeros = [n1, n2, n3]

    def jugar(self):
        numero_aleatorio = random.randint(1, 100)
        print("Numero generado:", numero_aleatorio)
        if numero_aleatorio in self.numeros:
            return ("Ganaste")
        else:
            return ("Perdiste")