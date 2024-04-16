import tkinter as tk
from Eleni_Classes import Epass

from ClassesAisthitirasTameio import *
from Stam_Classes_b import *

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("eap app")
		self.minsize(700, 400)
		self.start_screen = StartScreen(self)
		self.mainloop()


class StartScreen(tk.Frame):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

		self.configure(bg="#9403fc")

		self.start_button = tk.Button(self, text="αρχη", command=self.start)
		self.start_button.pack(expand=True)
		self.place(relheight=1, relwidth=1)

	def start(self):
		self.destroy()
		self.parent.main_screen = MainScreen(self.parent)


class MainScreen(tk.Frame):

	def __init__(self, parent):
		super().__init__(parent)

		self.results_button = None
		self.parent = parent
		self.attempted_passes = 0
		self.stat_string = tk.StringVar(self, "    \n    \n    ")

		self.configure(bg="#9403fc")

		self.next_button = tk.Button(self, text="επομενο", command=self.next_vehicle)
		self.next_button.pack(expand=True)

		self.car_stats = tk.Frame(self, bg="gray")
		self.car_id = tk.Label(self.car_stats, textvariable=self.stat_string)
		self.car_id.pack()
		self.car_stats.pack(expand=True)

		self.place(relheight=1, relwidth=1)

	def next_vehicle(self):
		current_epass = aisthitiras.anixneyei(ePassList)  # (αυτο πρεπει να κανει return random ePass απο την λιστα)

		current_vehicle = current_epass.oxima

		# (η elegxei περνει Input ενα ποσο και βγαζει True αν η καρτα εχει >= λεφτα)
		if current_epass.elegxei():

			current_epass.xrewnei()
			tameio.addAxiaDieleysis(current_vehicle.xrewnei())


		else:
			print("δεν εχει λεφτα ξερωγω λολ")
			current_epass.fortizei()
		self.attempted_passes += 1
		if self.attempted_passes >= 2:
			self.next_button.configure(state="disabled")
			self.results_button = tk.Button(self, text="αποτελεσματα", command=self.to_results)
			self.results_button.pack(expand=True)

		self.stat_string.set(
			f'{current_epass.kwdkartas}\n'
			f'{current_vehicle.arKykloforias}\n'
			f'{current_vehicle.__class__.__name__}')

	def to_results(self):
		self.destroy()
		self.parent.end_screen = EndScreen(self.parent)


class EndScreen(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		self.parent = parent

		self.configure(bg="#9403fc")

		self.end_button = tk.Button(self, text="τελος", command=parent.destroy)
		self.end_button.pack()

		self.end_stats_frame = tk.Frame(self, bg="gray")

		self.placeholder = tk.Label(self.end_stats_frame, text="edw tha leei pramata")
		self.placeholder.pack()

		self.end_stats_frame.pack(expand=True)

		self.place(relheight=1, relwidth=1)


tameio = Tameio()
aisthitiras = Aisthitiras(tameio)

ePassList = []
oximataList = []

vehiclesDict = [
				['1715', 'ΝΙΒ1000', 'Επιβατικό'],
				['2230', 'ΝΚΚ2113', 'Δίκυκλο'],
				['3934', 'ΝΙΟ3225', 'Φορτηγό'],
				['4141', 'PPE4789', 'Επιβατικό'],
				['5371', 'XAY5466', 'Επιβατικό'],
				['6642', 'XIE6472', 'Επιβατικό'],
				['7499', 'NZT7228', 'Φορτηγό'],
				['8107', 'NZK8331', 'Δίκυκλο'],
				['9503', 'NZK9112', 'Επιβατικό'],
				['9977', 'NZK9955', 'Φορτηγό']]

for i in range(len(vehiclesDict)):

	if vehiclesDict[i][2] == "Επιβατικό":
		oximataList.append(Epivatiko(vehiclesDict[i][1]))

	elif vehiclesDict[i][2] == "Δίκυκλο":
		oximataList.append(Dikyklo(vehiclesDict[i][1]))

	else:
		oximataList.append(Fortigo(vehiclesDict[i][1]))

	ePassList.append(Epass(vehiclesDict[i][0]))

	ePassList[-1].oxima = oximataList[-1]
	oximataList[-1].ePass = ePassList[-1]

app = App()

# αυτα θα φυγουν

print("διελευσεις:", tameio.arDieleysewn, "εσωδα", tameio.esodaDieleysewn)

for i in range(10):
	print("αριθμος κυκλοφοριας: ", oximataList[i].arKykloforias)
	print("αριθμος καρτας:", ePassList[i].kwdkartas, "    υποληπο καρτας", ePassList[i].ypoloipoLogariasmou)

