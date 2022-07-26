import leDatos as LD
import heuConAle as HCA

numObjetos = numMochilas = 0
vetValoresObjetos = []
vetPesosObjetos = []
vetCapacidadeMochilas = []
[numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas] = LD.leDatos()

#obteniendo una solucion constructiva aleatoria
sol = HCA.heuConstrutivaAleatoria(numObjetos, numMochilas)

print("Solucion: ", sol)