import leDatos as LD
import calcFO as CF
import BuscaTabu as BT
import heuConAle as HCA

numObjetos = numMochilas = 0
T=10 #en este ejemplo adoptamos el tamaño de 10 para la lista tabú
tempoExec = 10 #en este ejemplo adoptamos 10 segundos de tiempo de ejecución
vetValoresObjetos = []
vetPesosObjetos = []
vetCapacidadeMochilas = []
[numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas] = LD.leDatos()

solIni = HCA.heuConstrutivaAleatoria(numObjetos, numMochilas)

#obtención de una solución mediante la metaheurística de búsqueda tabú
[sol, tempo] = BT.buscaTabu(tempoExec, T, solIni, numObjetos, numMochilas, vetValoresObjetos,
vetPesosObjetos, vetCapacidadeMochilas)

#calculando el FO de la solución obtenida
FO = CF.calcFO(sol, numObjetos, numMochilas, vetValoresObjetos, vetPesosObjetos,
vetCapacidadeMochilas)

print("Solucion: ", sol)
print("FO: ", FO)
print("Encontrado en: %.2f " % tempo)