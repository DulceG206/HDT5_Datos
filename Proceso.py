import random

class Proceso:
    def __init__(self, env, nombre, sistema):
        self.env = env
        self.nombre = nombre
        self.sistema = sistema
        self.memoria_necesaria = random.randint(5, 20)

        