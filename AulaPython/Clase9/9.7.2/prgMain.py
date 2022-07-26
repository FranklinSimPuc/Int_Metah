import leDatos as LD
import heuConAle as HCA
import calcFO as CF
import heuPM as PM

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

#Realizando la mejor mejora
sol = PM.heuPrimeiraMelhora(sol, numObjetos, numMochilas, vetValoresObjetos,
vetPesosObjetos, vetCapacidadeMochilas)
#calculando la FO de la solucion obtenida
FO = CF.calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas)

print("Solucao: ", sol)
print("FO: ", FO)