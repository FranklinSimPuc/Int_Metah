ALFA = 1000

def calcFO(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc):
    fo = 0
    vetPes = [0] * numMoc

    for i in range(numObj):
        #calcula la FO de los objetos seleccionados
        if solucao[i] != 0:
            fo += valObj[i]
            vetPes[solucao[i]-1] += vetPesObj[i]

    for j in range(numMoc):
        #verifica si la capacidad de la mochila fue excedida
        if vetPes[j] > vetCapMoc[j]:
            #si es verdadero penaliza la FO
            fo -= ALFA*(vetPes[j] -  vetCapMoc[j])
            
    return fo