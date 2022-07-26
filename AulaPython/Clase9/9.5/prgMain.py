import leDatos as LD
import heuConAle as HCA
import calcFO as CF

numObjetos = numMochilas = 0
vetValoresObjetos = []
vetPesosObjetos = []
vetCapacidadeMochilas = []
[numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas] = LD.leDatos()

#obteniendo una solucion constructiva aleatoria
sol = HCA.heuConstrutivaAleatoria(numObjetos, numMochilas)

#calculando la FO de la solución obtenida
FO = CF.calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas)

print("Solucion: ", sol)
print("FO: ", FO)