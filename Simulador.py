import simpy
import random
import statistics
import matplotlib.pyplot as plt

RANDOM_SEED = 42

class Simulador:
    def __init__(self, num_procesos, intervalo, memoria_total, instrucciones_por_unidad, num_cpus):
        random.seed(RANDOM_SEED)
        
        self.env = simpy.Environment()
        self.num_procesos = num_procesos
        self.intervalo = intervalo
        self.memoria_total = memoria_total
        self.instrucciones_por_unidad = instrucciones_por_unidad
        
        self.cpu = simpy.Resource(self.env, capacity=num_cpus)
        self.ram = simpy.Container(self.env, init=memoria_total, capacity=memoria_total)
        
        self.tiempos = []

    def proceso(self, nombre):
        llegada = self.env.now
        
        memoria_necesaria = random.randint(1, 10)
        instrucciones_restantes = random.randint(1, 10)
        
        yield self.ram.get(memoria_necesaria)
        
        while instrucciones_restantes > 0:
            with self.cpu.request() as req:
                yield req
                
                ejecutar = min(self.instrucciones_por_unidad, instrucciones_restantes)
                yield self.env.timeout(1)
                
                instrucciones_restantes -= ejecutar
            
            if instrucciones_restantes > 0:
                if random.randint(1,21) == 1:
                    yield self.env.timeout(1)  
        
      
        yield self.ram.put(memoria_necesaria)
        
        salida = self.env.now
        self.tiempos.append(salida - llegada)

    def generador(self):
        for i in range(self.num_procesos):
            self.env.process(self.proceso(f"P{i}"))
            llegada = random.expovariate(1.0 / self.intervalo)
            yield self.env.timeout(llegada)

    def correr(self):
        self.env.process(self.generador())
        self.env.run()
        
        promedio = statistics.mean(self.tiempos)
        desviacion = statistics.stdev(self.tiempos) if len(self.tiempos) > 1 else 0
        
        return promedio, desviacion


def ejecutar_experimento(intervalo, memoria, velocidad_cpu, cpus):
    procesos_lista = [25,50,100,150,200]
    promedios = []
    
    for p in procesos_lista:
        sim = Simulador(p, intervalo, memoria, velocidad_cpu, cpus)
        prom, des = sim.correr()
        print(f"Procesos: {p} | Promedio: {prom:.2f} | Desv: {des:.2f}")
        promedios.append(prom)
    
    plt.figure()
    plt.plot(procesos_lista, promedios)
    plt.xlabel("Número de procesos")
    plt.ylabel("Tiempo promedio en el sistema")
    plt.title(f"Intervalo={intervalo}, Memoria={memoria}, CPU={cpus}, Vel={velocidad_cpu}")
    plt.show()


print("Intervalo 10")
ejecutar_experimento(intervalo=10, memoria=100, velocidad_cpu=3, cpus=1)

print("Intervalo 5")
ejecutar_experimento(intervalo=5, memoria=100, velocidad_cpu=3, cpus=1)

print("Intervalo 1")
ejecutar_experimento(intervalo=1, memoria=100, velocidad_cpu=3, cpus=1)

 # se hacen las mejoras en el código para comparar

print("Memoria 200")
ejecutar_experimento(intervalo=10, memoria=200, velocidad_cpu=3, cpus=1)


print("CPU más rápido")
ejecutar_experimento(intervalo=10, memoria=100, velocidad_cpu=6, cpus=1)


print("2 CPUs")
ejecutar_experimento(intervalo=10, memoria=100, velocidad_cpu=3, cpus=2) 