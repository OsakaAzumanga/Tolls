from testclasses import *
from Eleni_Classes import Bara, ePass
from Tkinter_Classes import *


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
		self.background = tk.Label(self, background="#9403fc")
		self.background.place(relx=0, rely=0, relheight=1, relwidth=1)
		self.start_button = tk.Button(self, text="αρχη", command=self.start)
		self.start_button.pack(expand=True)
		self.place(relheight=1, relwidth=1)

	def start(self):
		self.start_button.destroy()
		self.parent.main_screen = MainScreen(self.parent)


class MainScreen(tk.Frame):

	def __init__(self, parent):
		super().__init__(parent)

		self.parent = parent
		self.attempted_passes = 0
		self.stat_string = tk.StringVar(self, "NULL\nNULL\nNULL")

		self.background = tk.Label(self, background="#9403fc")
		self.background.place(relx=0, rely=0, relheight=1, relwidth=1)

		self.next_button = tk.Button(self, text="επομενο", command=self.next_vehicle)
		self.next_button.pack(expand=True)

		self.car_stats = tk.Frame(self, bg="gray")
		self.car_id = tk.Label(self.car_stats, textvariable=self.stat_string)
		self.car_id.pack()
		self.car_stats.pack()

		self.car_stats.pack(expand=True,)

		self.place(relheight=1, relwidth=1)

	def next_vehicle(self):
		current_epass = aisthitiras.anixneyei(ePassList)  # (αυτο πρεπει να κανει return random ePass απο την λιστα)

		current_vehicle = current_epass.oxima

		# (η elegxei περνει Input ενα ποσο και βγαζει True αν η καρτα εχει >= λεφτα)
		if current_epass.elegxei(current_vehicle):

			current_epass.xrewnei(current_vehicle)
			tameio.addAxiaDieleysis(current_vehicle)
			tollBar.anoigei()
			current_vehicle.dieleysei()

			tollBar.kleinei()
		else:
			print("δεν εχει λεφτα ξερωγω λολ")
			current_epass.fortizei()
		self.attempted_passes += 1
		if self.attempted_passes >= 20:
			self.next_button.configure(state="disabled")

		self.stat_string.set(f'{current_epass.kwdkartas}\n{current_vehicle.arKykloforias}\n{current_vehicle.__class__.__name__}')

	def to_results(self):
		pass


tameio = Tameio()
tollBar = Bara()
aisthitiras = Aisthitiras()


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

	ePassList.append(ePass(vehiclesDict[i][0]))

	ePassList[-1].oxima = oximataList[-1]
	oximataList[-1].epass = ePassList[-1]

app = App()


print("διελευσεις:", tameio.arDieleysewn, "εσωδα", tameio.esodaDieleysewn)

for i in range(10):
	print("αριθμος κυκλοφοριας: ", oximataList[i].arKykloforias)
	print("αριθμος καρτας:", ePassList[i].kwdkartas, "    υποληπο καρτας", ePassList[i].ypoloipoLogariasmou)
	print("αριθμος διελευσεων", oximataList[i].arDieleysewn, "\n\n")
