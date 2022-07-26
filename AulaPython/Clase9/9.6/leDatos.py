def leDatos():
    #inicializando las variables
    numObj = numMoc = 0
    valObj = []
    pesObj = []
    capMoc = []
    #leyenndo los datos
    f = open(r"C:\Users\Windows 10\Downloads\AulaPython\Clase9\9.6\dadosMochila1.txt", "r")
    #leyendo la primeira linea
    linea = f.readline()
    valores = linea.split()
    #leyendo el número de objetos
    numObj = int(valores[0])
    #leyendo el número de mochilas
    numMoc = int(valores[1])

    #leyendo la segunda linea
    linea = f.readline()
    valores = linea.split()
    #leyendo los valores de los objetos
    for val in valores:
        valObj.append(int(val))

    #leyendo la tercera linea
    linea = f.readline()
    valores = linea.split()
    #leyendo los pesos de los objetos
    for val in valores:
        pesObj.append(int(val))

    #leyendo la cuarta linea
    linea = f.readline()
    valores = linea.split()
    #leyendo las capacidades de las mochilas
    for val in valores:
        capMoc.append(int(val))

    f.close()
    return numObj, numMoc, valObj, pesObj, capMoc