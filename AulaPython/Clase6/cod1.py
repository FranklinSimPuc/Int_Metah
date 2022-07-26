f=open(r"C:\Users\Windows 10\Downloads\AulaPython\Clase6\dados1Aula.txt", "r")
linea=f.readline()
valores = linea.split()
print(valores)
numObjetos = int(valores[0])
numMochilas = int(valores[1])
print(numObjetos)
print(numMochilas)

#Lectura de la segunda linea
linea2=f.readline()
valores2 = linea2.split()
print(valores2)
vetValoresObjetos = []
for val in valores2:
    vetValoresObjetos.append(int(val))
print(vetValoresObjetos)

#Lectura siguiente lineas
linea3 = f.readline()
valores3 = linea3.split()
print(valores3)
vetPesosObjetos = []
for val in valores3:
    vetPesosObjetos.append(int(val))
print(vetPesosObjetos)

linea4 = f.readline()
valores4 = linea4.split()
vetCapacidadeMochilas = []
for val in valores4:
    vetCapacidadeMochilas.append(int(val))
print(vetCapacidadeMochilas)
f.close()