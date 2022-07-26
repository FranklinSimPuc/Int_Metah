import time
import calcFO as CF
import heuConAleGul as HCG
import heuPM as PM

def grasp(lrc, tempo, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc):
    ini = time.time()
    achouT = time.time()
    melhorFO = float("-inf") #obteniendo un valor infinito negativo
    lrc = int((lrc * numObj) / 100) #calculating LRC % basado en objetos
    mSol = [0] * numObj

    while 1:
        sol = HCG.heuConAleGul(lrc, numObj, numMoc, vetValObj, vetPesObj,
        vetCapMoc)

        #busca local
        sol = PM.heuPrimeiraMelhora(sol, numObj, numMoc, vetValObj, vetPesObj,
        vetCapMoc)
        FO = CF.calcFO(sol, numObj, numMoc, vetValObj, vetPesObj, vetCapMoc)

        if FO > melhorFO:
            mSol = sol
            melhorFO = FO
            achouT = time.time()

        fim = time.time()
        #verificar si debe continuar ejecutándose
        if fim <= (ini + tempo):
            continue
        else:   
            break

    return mSol, (achouT - ini)