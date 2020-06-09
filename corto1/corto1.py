#! /usr/bin/python3.8



N = 796

def tipodenumero(valor):
	if valor % 2 == 0:
		# print ('numero par')
		valor = valor // 2
	elif valor %2  !=0:
		# print ('numero impar')
		valor = 3*valor + 1

	return valor

def secuencia (G):
	h = []
	h.append(G)
	while G != 1:
		G = tipodenumero(G)
		h.append(G)
	return h


def escritura (fileName = 'collatz.txt'):
	archivo = open(fileName, 'w')
	archivo.write('Esper, calculando..')
	for i in range(2,N):
	        p = secuencia (i)
        	archivo.write(str(p))


escritura()




