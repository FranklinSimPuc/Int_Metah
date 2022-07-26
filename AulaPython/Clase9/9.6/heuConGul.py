import numpy as np

def heuConstrutivaGulosa(numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    sol = [0] * numObj
    #este vetor es utilizado para almacenar el peso asignado a cada mochila
    vetPes = [0] * numMoc

    #obteniendo los índices de los objetos ordenados (descendente)
    vAuxInd = np.argsort(vetValObj)[::-1]

    for i in range(numObj):
        #recorriendo los objetos
        for j in range(1, numMoc):
            #verificar si el objeto cabe en la mochila
            if (vetPes[j-1] + vetPesObj[vAuxInd[i]]) <= vetCapMoc[j-1]:
                sol[vAuxInd[i]] = j
                vetPes[j-1] += vetPesObj[vAuxInd[i]]
                break #si ha colocado el objeto en la mochila, salga

    return sol