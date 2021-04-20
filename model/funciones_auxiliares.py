import os
import pyfiglet
import socket

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

def textDecoration():
	print('-----------------------------------------------------------')
	ascii_banner = pyfiglet.figlet_format('Magic Cards')
	print(ascii_banner)
	print('V. 1.0')

def mostrarNumero(num):
	print('---------------------------------------------------------------------------')
	ascii_banner = pyfiglet.figlet_format('El numero es '+ str(num))
	print(ascii_banner)
	print('---------------------------------------------------------------------------')

def enviarNumero(num, direccion):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = (direccion, 10000)
	enviar = num
	message = bytes(enviar, 'utf-8')
	connection = False
	
	try:
		# Enviar data
		sock.sendto(message, server_address)
		# Recibir respuesta
		data, server = sock.recvfrom(4096)
		numeroSecreto = str(data, 'utf-8')
		connection = True

	except ConnectionResetError:
		print('-----------------------------------------------------------')
		print('El servidor no se encuentra disponible...')
	except:
		print('-----------------------------------------------------------')
		print('El servidor no se encuentra disponible...')
	finally:
		sock.close()
		return connection, numeroSecreto



	

	
