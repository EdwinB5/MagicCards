import os
import pyfiglet
import socket
import platform    # For getting the operating system name
import subprocess  # For executing a shell command


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

def ping(host, network_timeout=3):
    """Send a ping packet to the specified host, using the system "ping" command."""
    args = [
        'ping'
    ]

    platform_os = platform.system().lower()

    if platform_os == 'windows':
        args.extend(['-n', '1'])
        args.extend(['-w', str(network_timeout * 1000)])
    elif platform_os in ('linux', 'darwin'):
        args.extend(['-c', '1'])
        args.extend(['-W', str(network_timeout)])
    else:
        raise NotImplemented('Unsupported OS: {}'.format(platform_os))

    args.append(host)

    try:
        if platform_os == 'windows':
            output = subprocess.run(args, check=True, universal_newlines=True).stdout

            if output and 'TTL' not in output:
                return False
        else:
            subprocess.run(args, check=True)

        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False

	
