import time
import copy as cpy
import numpy as np
import calcFO as CF

def buscaTabu(tempo, T, solIni, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    ini = time.time()
    achouT = time.time()
    qtd = 0
    lista = np.zeros([2, T])
    mSol = solIni
    #calcular lq FO de la solución
    mFOGlobal = CF.calcFO(mSol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
    sol = cpy.copy(mSol)
    while 1:
        #mejor vecino
        mFO = float("-inf") #obteniendo un valor infinito negativo

        mO = -1
        mM = -1
        for i in range(numObj):
            moc = sol[i] # guardar la mochila actual del objeto
            for j in range(numMoc):
                #verificar la posición de la lista tabú
                pos = -1
                aspirou = 0
                for k in range(T):
                    if lista[0, k] == i and lista[1, k] == j:
                        pos = k
                        break

                if pos == -1:
                    #la configuración no está en la lista tabú
                    sol[i] = j
                    FO = CF.calcFO(sol, numObj, numMoc, vetValObj, vetPesObj,
                    vetCapMoc)
                    if FO > mFO:
                        mO = i
                        mM = j
                        mFO = FO
                else:
                    #esta en la lista tabu, pero FO es mejor que FO Global
                    sol[i] = j
                    FO = CF.calcFO(sol, numObj, numMoc, vetValObj, vetPesObj,
                    vetCapMoc)
                    if FO > mFOGlobal:
                        #aspiracion por objetivo
                        mO = i
                        mM = j
                        mFO = FO
                        #guardar una bandera para no volver a incluirla en la lista tabú
                        aspirou = 1
                #ajustando para mochila original
                sol[i] = moc

        #actualizando la lista Tabu
        if mO != -1:
            #algún vecino fue aceptado
            sol[mO] = mM #el objeto en la posición aceptada recibe la mejor mochila
            FO = mFO #actualiza la FO
            if (aspirou == 0): # no usó el criterio de aspiración
                lista[0, qtd] = mO
                lista[1, qtd] = mM
                qtd += 1
                if qtd >= T:
                    qtd = 0
        else:
            #no se aceptan vecinos
            sol[lista[0,0]] = lista[1,0] #realiza a aspiracao por default
            FO = CF.calcFO(sol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)

        if FO > mFOGlobal:
            mSol = cpy.copy(sol)
            achouT = time.time()

        fim = time.time()
        #verificar si debe continuar ejecutándose
        if fim <= (ini + tempo):
            continue
        else:
            break

    return mSol, (achouT - ini)