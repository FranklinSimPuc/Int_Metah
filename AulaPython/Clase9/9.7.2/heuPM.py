import calcFO as CF

def heuPrimeiraMelhora(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc):
    while 1:
        # obtener el FO de la solución actual
        mFO = CF.calcFO(solucao, numObj, numMoc, valObj, vetPesObj, vetCapMoc)
        #inicializa la variable de control de interrupción de búsqueda
        melhorou = False

        for i in range(numObj):
            mAtual = solucao[i] #guarda la mochila actual
            for j in range(numMoc):
                solucao[i] = j #cambia la mochila y calcula el FO con la nueva solución
                FOAtual = CF.calcFO(solucao, numObj, numMoc, valObj, vetPesObj,
                vetCapMoc)
                if FOAtual > mFO: #si mejoras entonces guarda la información
                    melhorou = True #registro que mejoró
                    mFO = FOAtual #guarda la mejor FO
                    break #salir del bucle de la mochila

            if melhorou:
                break #salir del bucle del objeto
            else:
                solucao[i] = mAtual #restaurar mochila actual

        if not melhorou: #si no mejora, deténgase
            break

    return solucao