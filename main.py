from model.funciones_auxiliares import *
from model.magic_cards import *

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