import numpy as np
import random as rand

#generando la semilla
rand.seed()

def heuConAleGul(lrc, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    #montando el LRC
    vetAux = [0] * numObj
    vetVal = [0] * lrc
    vetLrc = [0] * lrc
    for i in range(lrc):
        obj = rand.randint(0, numObj-1)
        while vetAux[obj] == 1: #previene el sorteo de un número repetido
            obj = rand.randint(0, numObj-1)

        vetLrc[i] = obj
        vetVal[i] = vetValObj[obj]
        vetAux[obj] = 1

    #insertar objetos LRC en la mochila de forma codiciosa
    #obteniendo los índices de los objetos ordenados (descendente)
    vAuxIndLRC = np.argsort(vetVal)[::-1]
    sol = [0] * numObj
    vetPes = [0] * numMoc
    for i in range(lrc):
        for j in range(numMoc):
            if (vetPes[j] + vetPesObj[vetLrc[vAuxIndLRC[i]]]) <= vetCapMoc[j]:
                sol[vetLrc[vAuxIndLRC[i]]] = j
                vetPes[j] = vetPes[j] + vetPesObj[vetLrc[vAuxIndLRC[i]]]
                break

    #insertar los otros objetos en la mochila de forma codiciosa
    vAuxIndObj = np.argsort(vetValObj)[::-1]
    for i in range(numObj):
        if vetAux[vAuxIndObj[i]] == 0: #si es cierto, entonces aún no se ha asignado

            for j in range(numMoc):
                if (vetPes[j] + vetPesObj[vAuxIndObj[i]]) <= vetCapMoc[j]:
                    sol[vAuxIndObj[i]] = j
                    vetPes[j] = vetPes[j] + vetPesObj[vAuxIndObj[i]]
                    break
    return sol