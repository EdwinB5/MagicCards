from tkinter import *

class AppMagic:

	def __init__(self, root):
		root.title("MagicCards")
		root.resizable(False,False)
		root.iconbitmap("img/icon_cards.ico")
		root.config(bg="black")
		
		window_width, window_height = 960,540
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()

		position_top = int(screen_height/2 - window_height/2)
		position_right = int(screen_width/2 - window_width/2)

		root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
		
def volverInicio(root):
		root.destroy()
		mainWindow()

def gameWindow():
	gameRoot = Tk()
	AppMagic(gameRoot)

	mainFrame = Frame()
	mainFrame.pack()
	mainFrame.config(bg="black")
	mainFrame.config(width="960",height="540")

	Label(mainFrame, text="Primera carta", fg="white", bg="black", font=("Courier", 30)).grid(row="1", column="1", columnspan="8", pady="30")

	Button(mainFrame, text="Volver", command=lambda:volverInicio(gameRoot), width="25", height="1", font=("Courier", 15), 
		borderwidth="4", relief="raised", cursor="hand2").place(x=325,y=300)

	Label

	gameRoot.mainloop()

def helpWindow():
	helpRoot = Tk()
	AppMagic(helpRoot)

	mainFrame = Frame()
	mainFrame.pack()
	mainFrame.config(bg="black")
	mainFrame.config(width="960",height="540")

	Button(mainFrame, text="Volver", command=lambda:volverInicio(helpRoot), width="25", height="1", font=("Courier", 15), 
		borderwidth="4", relief="raised", cursor="hand2").place(x=325,y=300)

	helpRoot.mainloop()

def mainWindow():
	root = Tk()
	AppMagic(root)

	mainFrame = Frame()
	mainFrame.pack()
	mainFrame.config(bg="black")
	mainFrame.config(width="960",height="540")

	def botonIniciar():
		root.destroy()
		gameWindow()

	def botonManual():
		root.destroy()
		helpWindow()

	def botonSalir():
		root.destroy()

	Label(mainFrame, text="Magic Cards", fg="white", bg="black", font=("Courier", 75), borderwidth="25", 
		relief="sunken", justify="center").place(x=130,y=60)

	Button(mainFrame, text="Iniciar", command=botonIniciar, width="25", height="1", font=("Courier", 15), 
		borderwidth="4", relief="raised", cursor="hand2").place(x=325,y=300)

	Button(mainFrame, text="Manual de usuario", command=botonManual, width="25", height="1", font=("Courier", 15), 
		borderwidth="4", relief="raised", cursor="hand2").place(x=325,y=360)

	Button(mainFrame, text="Salir", command=botonSalir, width="25", height="1", font=("Courier", 15), 
		borderwidth="4", relief="raised", cursor="hand2").place(x=325,y=420)

	root.mainloop()

if __name__ == '__main__':
	mainWindow()
	