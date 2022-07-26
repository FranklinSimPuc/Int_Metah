import time
import math as mat
import copy as cpy
import random as rand
import calcFO as CF

#generando la semilla
rand.seed()

def SimulatedAnnealing(samax, ti, tc, tx, solIni, numObj, numMoc, vetValObj,
    vetPesObj, vetCapMoc):
    ini = time.time()
    achouT = time.time()
    # guardar la solución inicial como la mejor
    mSol = solIni
    mFO = CF.calcFO(mSol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
    #atribuir la mejor solución al sol actual
    sol = cpy.copy(mSol)
    FO = CF.calcFO(sol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
    #inicializa la temperatura
    temp = ti
    while temp > tc:
        #mientras que la temperatura inicial es más alta que la temperatura de congelación
        for i in range(samax):
            #solución vecina comienza desde la solución actual
            vSol = cpy.copy(sol)
            #generar una solucion vecina
            vSol[rand.randint(0, numObj-1)] = rand.randint(0, numMoc)
            #calcular el FO de la solución vecina
            vFO = CF.calcFO(vSol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)
            #calculando la variacion
            delta = FO - vFO

            if delta < 0:
                # si la variación es negativa entonces aceptar
                sol = cpy.copy(vSol)
                if vFO > mFO:
                    #si la FO del vecino es mejor que el FO del global FO acepta
                    mSol = cpy.copy(vSol)
                    achouT = time.time()
            else:
                if rand.random() < mat.exp(-(FO - vFO) / temp):
                    #si no es mejor pero se acepta empeorar
                    sol = cpy.copy(vSol)

        #enfría la temperatura
        temp *= tx

    return mSol, (achouT - ini)