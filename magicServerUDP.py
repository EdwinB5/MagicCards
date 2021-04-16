import socket
import pyfiglet

"""
Números en binario (1-100)

0.  0000000	16. 0010000	32. 0100000	48. 0110000	64. 1000000	80. 1010000	96.  1100000 112.1110000
1.  0000001	17. 0010001	33. 0100001	49. 0110001	65. 1000001	81. 1010001	97.	 1100001 113.1110001
2.  0000010	18. 0010010	34. 0100010	50. 0110010	66. 1000010	82. 1010010	98.	 1100010 114.1110010
3.  0000011	19. 0010011	35. 0100011	51. 0110011	67.	1000011	83. 1010011	99.  1100011 115.1110011
4.  0000100	20. 0010100	36. 0100100	52. 0110100	68.	1000100	84. 1010100	100. 1100100 116.1110100
5.  0000101	21. 0010101	37. 0100101	53. 0110101	69. 1000101	85. 1010101	101. 1100101 117.1110101
6.  0000110	22. 0010110	38. 0100110	54. 0110110	70.	1000110	86. 1010110	102. 1100110 118.1110110
7.  0000111	23. 0010111	39. 0100111	55. 0110111	71.	1000111	87. 1010111	103. 1100111 119.1110111
8.  0001000	24. 0011000	40. 0101000	56. 0111000	72. 1001000	88. 1011000	104. 1101000 120.1111000
9.  0001001	25. 0011001	41. 0101001	57. 0111001	73. 1001001	89. 1011001	105. 1101001 121.1111001
10. 0001010	26. 0011010	42. 0101010	58. 0111010	74. 1001010	90.	1011010	106. 1101010 122.1111010
11. 0001011	27. 0011011	43. 0101011	59. 0111011	75. 1001011	91.	1011011	107. 1101011 123.1111011
12. 0001100	28. 0011100	44. 0101100	60. 0111100	76. 1001100	92. 1011100	108. 1101100 124.1111100
13. 0001101	29. 0011101	45. 0101101	61. 0111101	77. 1001101	93. 1011101	109. 1101101 125.1111101
14. 0001110	30. 0011110	46. 0101110	62. 0111110	78.	1001110	94. 1011110	110. 1101110 126.1111110
15. 0001111	31. 0011111	47. 0101111	63. 0111111	79. 1001111	95.	1011111	111. 1101111 127.1111111

"""

def diccionarioBinario(numeroBinario):

	diccionarioBinario = {'0000000':'0','0000001':'1','0000010':'2','0000011':'3','0000100':'4','0000101':'5'
						,'0000110':'6','0000111':'7','0001000':'8','0001001':'9','0001010':'10','0001011':'11'
						,'0001100':'12','0001101':'13','0001110':'14','0001111':'15','0010000':'16'
						,'0010001':'17','0010010':'18','0010011':'19','0010100':'20','0010101':'21'
						,'0010110':'22','0010111':'23','0011000':'24','0011001':'25','0011010':'26'
						,'0011011':'27','0011100':'28','0011101':'29','0011110':'30','0011111':'31'
						,'0100000':'32','0100001':'33','0100010':'34','0100011':'35','0100100':'36'
						,'0100101':'37','0100110':'38','0100111':'39','0101000':'40','0101001':'41'
						,'0101010':'42','0101011':'43','0101100':'44','0101101':'45','0101110':'46'
						,'0101111':'47','0110000':'48','0110001':'49','0110010':'50','0110011':'51'
						,'0110100':'52','0110101':'53','0110110':'54','0110111':'55','0111000':'56'
						,'0111001':'57','0111010':'58','0111011':'59','0111100':'60','0111101':'61'
						,'0111110':'62','0111111':'63','1000000':'64','1000001':'65','1000010':'66'
						,'1000011':'67','1000100':'68','1000101':'69','1000110':'70','1000111':'71'
						,'1001000':'72','1001001':'73','1001010':'74','1001011':'75','1001100':'76'
						,'1001101':'77','1001110':'78','1001111':'79','1010000':'80','1010001':'81'
						,'1010010':'82','1010011':'83','1010100':'84','1010101':'85','1010110':'86'
						,'1010111':'87','1011000':'88','1011001':'89','1011010':'90','1011011':'91'
						,'1011100':'92','1011101':'93','1011110':'94','1011111':'95','1100000':'96'
						,'1100001':'97','1100010':'98','1100011':'99','1100100':'100','1100101':'101'
						,'1100110':'102','1100111':'103','1101000':'104','1101001':'105','1101010':'106'
						,'1101011':'107','1101100':'108','1101101':'109','1101110':'110','1101111':'111'
						,'1110000':'112','1110001':'113','1110010':'114','1110011':'115','1110100':'116'
						,'1110101':'117','1110110':'118','1110111':'119','1111000':'120','1111001':'121'
						,'1111010':'122','1111011':'123','1111100':'124','1111101':'125','1111110':'126'
						,'1111111':'127'}


	key = numeroBinario
	numeroSecreto = str(diccionarioBinario[key])
	return numeroSecreto
	
	"""
	for key in diccionarioBinario:
		cadena = str(key)
		if(cadena[7]=='1'):
			print(diccionarioBinario[key])
		#print (key,":",diccionarioBinario[key])
	"""
def tituloServidor():
	print('---------------------------------------------------------------')
	ascii_banner = pyfiglet.figlet_format('Servidor UDP')
	print(ascii_banner)
	print('---------------------------------------------------------------')

# Creación del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Uniendo el socket al puerto
tituloServidor()
server_address = ('localhost', 10000)
print('Iniciando el servidor {} en el puerto {}'.format(*server_address))
sock.bind(server_address)
print('---------------------------------------------------------------')

while True:
    print('\nEsperando una solicitud...')
    data, address = sock.recvfrom(4096)
    print('Recibiendo {} bytes de la dirección {}'.format(
        len(data), address))
    print(data)
    print('---------------------------------------------------------------')

    key = str(data, 'utf-8')

    numeroSecreto = diccionarioBinario(key)

    data = bytes(numeroSecreto, 'utf-8')

    if data:
        sent = sock.sendto(data, address)
        print('Enviando respuesta {} bytes devuelta a la dirección {}'.format(
            sent, address))