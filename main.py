import sys
from model.funciones_auxiliares import *
from model.magic_cards import *

def iniciarPrograma():
	conexion = False
	startProgram = False
	textDecoration()
	print('-----------------------------------------------------------')
	while not conexion:
		print('Comprobando conexión con el servidor...')
		conexion = enviarNumero('0000000')
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
	numeroSecreto = "";

	iniciarPrograma()
	clear()

	textDecoration()
	cartaUno()
	numeroSecreto += str(numeroEnCarta())
	clear()
	
	textDecoration()
	cartaDos()
	numeroSecreto += str(numeroEnCarta())
	clear()
	
	textDecoration()
	cartaTres()
	numeroSecreto += str(numeroEnCarta())
	clear()
	
	textDecoration()
	cartaCuatro()
	numeroSecreto += str(numeroEnCarta())
	clear()
	
	textDecoration()
	cartaCinco()
	numeroSecreto += str(numeroEnCarta())
	clear()
	
	textDecoration()
	cartaSeis()
	numeroSecreto += str(numeroEnCarta())
	clear()
	
	textDecoration()
	cartaSiete()
	numeroSecreto += str(numeroEnCarta())
	clear()

	numeroSecreto = ''.join(reversed(numeroSecreto))

	enviarNumero(numeroSecreto)

if __name__ == "__main__":
    main()