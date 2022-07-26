import leDatos as LD
import calcFO as CF
import SimulatedAnnealing as SA
import heuConAle as HCA

numObjetos = numMochilas = 0
vetValoresObjetos = []
vetPesosObjetos = []
vetCapacidadeMochilas = []
[numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas] = LD.leDatos()

solIni = HCA.heuConstrutivaAleatoria(numObjetos, numMochilas)

samax = ((numMochilas + 1) * numObjetos) * 1
tempInicial = 100
tempCongelamento = 0.01
txResfriamento = 0.975

#Obtener una solución mediante la metaheurística de recocido simulado
[sol, tempo] = SA.SimulatedAnnealing(samax, tempInicial, tempCongelamento, txResfriamento, solIni,
             numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos, vetCapacidadeMochilas)

#calculando la FO de la solución obtenida
FO = CF.calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas)

print("Solucion: ", sol)
print("FO: ", FO)
print("Encontrado en: %.2f " % tempo)