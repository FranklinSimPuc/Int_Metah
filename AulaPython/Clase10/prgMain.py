import leDatos as LD
import calcFO as CF
import grasp as GR

numObjetos = numMochilas = 0
LRC = 50 #en este ejemplo se adoptó un LRC del 50% de los objetos
tempoExec = 10 #en este ejemplo adoptamos 10 segundos de tiempo de ejecución
vetValoresObjetos = []
vetPesosObjetos = []
vetCapacidadeMochilas = []
[numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas] = LD.leDatos()

#obteniendo una solución por la metaheurística GRASP
[sol, tempo] = GR.grasp(LRC, tempoExec, numObjetos, numMochilas, vetValoresObjetos,
vetPesosObjetos, vetCapacidadeMochilas)

#calculando el FO de la solución obtenida
FO = CF.calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas)

print("Solucion: ", sol)
print("FO: ", FO)
print("Encontrado en: %.2f " % tempo)