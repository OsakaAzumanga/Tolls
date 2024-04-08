import tkinter as tk


def next_car():
	pass


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("eap app")
		self.minsize(700, 400)
		self.startscreen = StartScreen(self)
		self.mainloop()


class StartScreen(tk.Frame):

	def __init__(self, parent):
		super().__init__(parent)
		self.background = tk.Label(self, background="#9403fc")
		self.background.place(relx=0, rely=0, relheight=1, relwidth=1)
		self.startbutton = tk.Button(self, text="αρχη", command=self.start)
		self.startbutton.pack(expand=True)
		self.place(relheight=1, relwidth=1)

	def start(self):
		self.startbutton.destroy()
		nextvehicle()
