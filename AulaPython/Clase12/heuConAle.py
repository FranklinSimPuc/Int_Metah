import random as rand
#generando la semilla
rand.seed()

def heuConstrutivaAleatoria(numObj, numMoc):
    #inicializando el vector solucion con el tamaño del número de objetos
    sol = [0] * numObj
    for i in range(numObj):
        #Para cada objeto y sorteado
        #en que mochila se ubicara
        sol[i] = rand.randint(0, numMoc)

    return sol
