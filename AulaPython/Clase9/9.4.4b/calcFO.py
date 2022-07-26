def calcFO(solucao, valObj, numObj):
    fo = 0
    #ejecuta un buble recorriendo los objetos
    for i in range(numObj):
        #calcula la FO de los objetos seleccionados solo si fue asignado a una mochila
        if solucao[i] != 0:
            fo += valObj[i]
    return fo