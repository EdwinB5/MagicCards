import socket

def mostrarCarta(matriz, n):
	print('-----------------------------------------------------------')
	print('Carta número '+ str(n))
	print('-----------------------------------------------------------')
	b=''
	for fila in range(8):
		for columna in range(8):
			#print(matriz[fila][columna])
			b+=str(matriz[fila][columna])+ '\t'
		print(b)
		b=''
	print('-----------------------------------------------------------')
	
def cartaUno():
	cartaUno = [
				[1,17,33,49,65,81,97,113],
				[3,19,35,51,67,83,99,115],
				[5,21,37,53,69,85,101,117],
				[7,23,39,55,71,87,103,119],
				[9,25,41,57,73,89,105,121],
				[11,27,43,59,75,91,107,123],
				[13,29,45,61,77,93,109,125],
				[15,31,47,63,79,95,111,127]
				]

	mostrarCarta(cartaUno, 1)

def cartaDos():
	cartaDos = [
				[2,18,34,50,66,82,98,114],
				[3,19,35,51,67,83,99,115],
				[6,22,38,54,70,86,102,118],
				[7,23,39,55,71,87,103,119],
				[10,26,42,58,74,90,106,122],
				[11,27,43,59,75,91,107,123],
				[14,30,46,62,78,94,110,126],
				[15,31,47,63,79,95,111,127]
				]

	mostrarCarta(cartaDos, 2)

def cartaTres():
	cartaTres = [
				[4,20,36,52,68,84,100,116],
				[5,21,37,53,69,85,101,117],
				[6,22,38,54,70,86,102,118],
				[7,23,39,55,71,87,103,119],
				[12,28,44,60,76,92,108,124],
				[13,29,45,61,77,93,109,125],
				[14,30,46,62,78,94,110,126],
				[15,31,47,63,79,95,111,127]
				]

	mostrarCarta(cartaTres, 3)

def cartaCuatro():
	cartaCuatro = [
					[8,24,40,56,72,88,104,120],
					[9,25,41,57,73,89,105,121],
					[10,26,42,58,74,90,106,122],
					[11,27,43,59,75,91,107,123],
					[12,28,44,60,76,92,108,124],
					[13,29,45,61,77,93,109,125],
					[14,30,46,62,78,94,110,126],
					[15,31,47,63,79,95,111,127]
					]

	mostrarCarta(cartaCuatro, 4)

def cartaCinco():
	cartaCinco = [
					[16,24,48,56,80,88,112,120],
					[17,25,49,57,81,89,113,121],
					[18,26,50,58,82,90,114,122],
					[19,27,51,59,83,91,115,123],
					[20,28,52,60,84,92,116,124],
					[21,29,53,61,85,93,117,125],
					[22,30,54,62,86,94,118,126],
					[23,31,55,63,87,95,119,127]
					]

	mostrarCarta(cartaCinco, 5)

def cartaSeis():
	cartaSeis = [
				[32,40,48,56,96,104,112,120],
				[33,41,49,57,97,105,113,121],
				[34,42,50,58,98,106,114,122],
				[35,43,51,59,99,107,115,123],
				[36,44,52,60,100,108,116,124],
				[37,45,53,61,101,109,117,125],
				[38,46,54,62,102,110,118,126],
				[39,47,55,63,103,111,119,127]
				]

	mostrarCarta(cartaSeis, 6)

def cartaSiete():
	cartaSiete = [
					[64,72,80,88,96,104,112,120],
					[65,73,81,89,97,105,113,121],
					[66,74,82,90,98,106,114,122],
					[67,75,83,91,99,107,115,123],
					[68,76,84,92,100,108,116,124],
					[69,77,85,93,101,109,117,125],
					[70,78,86,94,102,110,118,126],
					[71,79,87,95,103,111,119,127]
					]

	mostrarCarta(cartaSiete, 7)

def enviarNumero(num):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ('localhost', 10000)
	enviar = num
	message = bytes(enviar, 'utf-8')
	connection = False
	
	try:
		# Enviar data
		print('Enviando {!r}'.format(message))
		sock.sendto(message, server_address)
		# Recibir respuesta
		print('Esperando respuesta del servidor...')
		data, server = sock.recvfrom(4096)
		numeroSecreto = str(data, 'utf-8')
		print('El número secreto es: ' + numeroSecreto)
		connection = True

	except ConnectionResetError:
		print("El servidor no se encuentra disponible...")

	finally:
		print('Cerrando el socket')
		sock.close()
		return connection
    	
    	

	
