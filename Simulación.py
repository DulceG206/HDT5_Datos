import math
import simpy
import random 

memoria = 100
velocidad_procesador = 5
numero_procesadores = 2
intervalosTiempo = 5 



def main():
    env = simpy.Environment()

    memoria = simpy.Container(env, init=MEMORIA_TOTAL, capacity=MEMORIA_TOTAL)
    cpu = simpy.Resource(env, capacity=NUMERO_PROCESADORES)

    num_procesos = 25

    for i in range(num_procesos):
        env.process(proceso(env, f"Proceso {i+1}", memoria, cpu))

    env.run()