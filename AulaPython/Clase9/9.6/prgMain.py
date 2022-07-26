import leDatos as LD
import heuConGul as HCG
import calcFO as CF

numObjetos = numMochilas = 0
vetValoresObjetos = []
vetPesosObjetos = []
vetCapacidadeMochilas = []
[numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas] = LD.leDatos()

#obteniendo una solucion constructiva aleatoria
sol = HCG.heuConstrutivaGulosa(numObjetos, numMochilas, vetValoresObjetos,
vetPesosObjetos, vetCapacidadeMochilas)

#calculando la FO de la solución obtenida
FO = CF.calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas)

print("Solucion: ", sol)
print("FO: ", FO)