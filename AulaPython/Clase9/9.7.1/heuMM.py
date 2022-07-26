import calcFO as CF

def heuMelhorMelhora(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc):
    while 1:
        # obtener el FO de la solución actual
        mFO = CF.calcFO(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc)
        #inicializa las variables que almacenarán el control de intercambio de objetos y mochilas
        mO = -1
        mM = -1

        for i in range(numObj):
            mAtual = solucao[i] #guarda la mochila atual
            for j in range(numMoc):
                solucao[i] = j #cambia la mochila y calcula el FO de la nueva solución
                FOAtual = CF.calcFO(solucao, numObj, numMoc, valObj, vetPesObj,
                vetCapMoc)
                if FOAtual > mFO: #si mejora entonces guarda las posiciones
                    mO = i
                    mM = j
                    mFO = FOAtual

            solucao[i] = mAtual #restaura la mochila actual

        if mO != -1: #si es verdadero entonces hubo mejora
            solucao[mO] = mM #guardar la mejora que se produjo
        else:
            break #si no hay forma de mejorar, termínalo
  
    return solucao