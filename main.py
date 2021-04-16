import sys
from model.funciones_auxiliares import *
from model.magic_cards import *

def iniciarPrograma():
	conexion = False
	startProgram = False
	direccion_servidor = ""
	textDecoration()
	print('-----------------------------------------------------------')
	while not conexion:
		direccion_servidor = str(input('Introduzca la dirección del servidor: '))
		print('-----------------------------------------------------------')
		print('Comprobando conexión con el servidor...')
		conexion, numeroSecret = enviarNumero('0000000', direccion_servidor)
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

def finalizarPrograma():
	
	cerrar = False

	while not cerrar:
		entrada = str(input(("Desea reiniciar el programa? [y/N]: ")))
		if (entrada.lower() == 'y' or entrada.lower() == "yes"):
			cerrar = True
		elif (entrada.lower()=='n' or entrada.lower() == 'no'):
			print('---------------------------------------------------------------------------')
			print("El programa se esta cerrando...")
			print('---------------------------------------------------------------------------')
			sys.exit()
		else:
			print('---------------------------------------------------------------------------')
			print("Opción no valida, intente otra vez...")
			print('---------------------------------------------------------------------------')
	if cerrar:
		main()

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
	try:

		clear()
		address = iniciarPrograma()
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

		conexion, numeroSecreto = enviarNumero(numeroSecreto, address)

		mostrarNumero(numeroSecreto)

		finalizarPrograma()

	except UnboundLocalError:
		pass

if __name__ == "__main__":
    main()


