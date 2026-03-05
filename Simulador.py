import simpy
import random
from Proceso import Procesos

random_seed = 42

class Simulador:

    def __init__(self, env, num_procesadores, memoria_total, procesos, intervalo_tiempo):
        self.env = env
        self.num_procesadores = num_procesadores
        self.memoria_total = memoria_total
        self.memoria_disponible = memoria_total
        self.procesos = procesos
        self.intervalo_tiempo = intervalo_tiempo

        def generar_procesos(self):
            