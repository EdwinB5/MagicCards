import sys
from model.funciones_auxiliares import *
from model.magic_cards import *

def iniciarPrograma():
	clear()
	conexion = False
	startProgram = False
	direccion_servidor = ""
	textDecoration()
	print('-----------------------------------------------------------')
	while not conexion:
		direccion_servidor = str(input('Introduzca la dirección del servidor: '))
		print('-----------------------------------------------------------')
		print('Comprobando conexión con el servidor...')
		#conexion, numeroSecret = enviarNumero('0000000', direccion_servidor)
		conexion = ping(direccion_servidor)
		print('-----------------------------------------------------------')
		if conexion:
			while not startProgram:
				entrada = str(input(('El servidor esta conectado, desea iniciar el programa [y/N]: ')))
				if (entrada.lower() == 'y' or entrada.lower() == 'yes'):
					startProgram = True
				elif(entrada.lower() == 'n' or entrada.lower() == 'no'):
					sys.exit()
				else:
					print('-----------------------------------------------------------')
					print('El valor introducido no es valido, intente otra vez...')
					print('-----------------------------------------------------------')
		elif(conexion == False):
			print('El servidor no se encuentra disponible, compruebe que el servidor este disponible e intente otra vez...')
			sys.exit()
	return direccion_servidor

def programaEnCurso(i,address):
	numeroSecreto = ""
	for i in range(7):
		clear()
		textDecoration()
		selectorCarta(i)
		numeroSecreto += str(numeroEnCarta())
	numeroSecreto = ''.join(reversed(numeroSecreto))
	conexion, numeroSecreto = enviarNumero(numeroSecreto, address)

	clear()
	mostrarNumero(numeroSecreto)


def finalizarPrograma():
	
	cerrar = False

	while not cerrar:
		entrada = str(input(("Desea reiniciar el programa? [y/N]: ")))
		if (entrada.lower() == 'y' or entrada.lower() == "yes"):
			cerrar = False
			return False
		elif (entrada.lower()=='n' or entrada.lower() == 'no'):
			print('---------------------------------------------------------------------------')
			print("El programa se esta cerrando...")
			print('---------------------------------------------------------------------------')
			return True
		else:
			print('---------------------------------------------------------------------------')
			print("Opción no valida, intente otra vez...")
			print('---------------------------------------------------------------------------')
	if cerrar:
		return True


def numeroEnCarta():
	respuestaValida = False
	while not respuestaValida:
		opcion = str(input('¿El número se encuentra en esta carta? [y/N]: '))
		if (opcion.lower() == 'y' or opcion.lower() == 'yes'):
			respuesta = 1
			respuestaValida = True
		elif (opcion.lower() == 'n' or opcion.lower() == 'no'):
			respuesta = 0
			respuestaValida = True
		else:
			print('-----------------------------------------------------------')
			print('Opción no valida, intente otra vez...')
			print('-----------------------------------------------------------')

	return respuesta

def main():
	i = 0
	address = iniciarPrograma()
	cerrar = False
	while not cerrar:
		programaEnCurso(i, address)

		cerrar = finalizarPrograma()
	
if __name__ == "__main__":
    main()


