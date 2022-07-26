import numpy as np
datosAlumnos = np.genfromtxt(r"C:\Users\Windows 10\Downloads\AulaPython\Clase6\dados2Aula.csv",
dtype=None, delimiter=";", encoding=None,skip_header=1, names=('Matricula', 'Nome', 'Idade', 'Nota1', 'Nota2', 'Nota3'))
print(datosAlumnos)

np.savetxt(r"C:\Users\Windows 10\Downloads\AulaPython\Clase6\teste.txt", datosAlumnos, fmt='%s')