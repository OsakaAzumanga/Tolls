import tkinter as tk
from Classes_Epass import Epass
from ClassesAisthitirasTameio import *
from Classes_Oxima_Epivatiko_Dikyklo_Fortigo import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import randint
import time as time
from pathlib import Path

directory = Path(__file__).absolute().parent


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("eap app")
		self.minsize(720, 600)
		self.start_screen = StartScreen(self)

		icon = tk.PhotoImage(file=f"{directory}\\assets\\euro.png")
		self.iconphoto(True, icon)

		self.mainloop()


class StartScreen(tk.Frame):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

		self.configure(bg="#FFFFFF")

		self.start_button = tk.Button(self, text="Έναρξη", command=self.start)
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

		self.configure(bg="#FFFFFF")

		self.car_stats = tk.Frame(self, bg="gray")
		self.car_id = tk.Label(self.car_stats, textvariable=self.stat_string, width=25, height=5)
		self.car_id.pack()
		self.car_stats.pack(expand=True)

		self.loading_icons = []
		for image_number in range(12):
			self.loading_icons.append(tk.PhotoImage(file=f"{directory}\\assets\\loading_bar\\Frame {image_number+1}.png"))
		self.Epivatiko_pass_image = tk.PhotoImage(file=f"{directory}\\assets\\paint\\car_pass.png")
		self.Epivatiko_nopass_image = tk.PhotoImage(file=f"{directory}\\assets\\paint\\car_nopass.png")
		self.Dikyklo_pass_image = tk.PhotoImage(file=f"{directory}\\assets\\paint\\moto_pass.png")
		self.Dikyklo_nopass_image = tk.PhotoImage(file=f"{directory}\\assets\\paint\\moto_nopass.png")
		self.Fortigo_pass_image = tk.PhotoImage(file=f"{directory}\\assets\\paint\\truck_pass.png")
		self.Fortigo_nopass_image = tk.PhotoImage(file=f"{directory}\\assets\\paint\\truck_nopass.png")
		self.hello_image = tk.PhotoImage(file=f"{directory}\\assets\\paint\\hello.png")

		self.image_label = tk.Label(self, image=self.hello_image)
		self.image_label.pack(expand=True)

		self.controls = tk.Frame(self, bg="dark gray")

		self.next_button = tk.Button(self.controls, text="Επόμενο", command=self.wait_for_vehicle)
		self.next_button.pack(expand=True)

		self.results_button = tk.Button(self.controls, text="Αποτελέσματα", command=self.to_results, state="disabled")
		self.results_button.pack(expand=True)

		self.controls.pack(expand=True, fill="both")

		self.place(relheight=1, relwidth=1)

	def wait_for_vehicle(self):
		self.stat_string.set("Έλεγχος οχήματος")
		self.next_button.configure(state="disabled")
		random_loops = randint(2, 7)

		for loop in range(random_loops):
			for frame in range(12):

				time.sleep(0.00)

				self.image_label.configure(image=self.loading_icons[frame])
				self.image_label.image = self.loading_icons[frame]
				self.update()
		self.next_vehicle()

	def next_vehicle(self):
		self.next_button.configure(state="normal")
		current_epass = aisthitiras.anixneyei(ePassList)  # (αυτο πρεπει να κανει return random ePass απο την λιστα)

		current_vehicle = current_epass.oxima

		# (η elegxei περνει Input ενα ποσο και βγαζει True αν η καρτα εχει >= λεφτα)
		if current_epass.elegxei():

			pass_string = "Επαρκές ποσό"

			if isinstance(current_vehicle, Epivatiko):
				current_image = self.Epivatiko_pass_image
			elif isinstance(current_vehicle, Dikyklo):
				current_image = self.Dikyklo_pass_image
			else:
				current_image = self.Fortigo_pass_image

			self.image_label.configure(image=current_image)
			self.update()

			current_epass.xrewnei()
			tameio.addAxiaDieleysis(current_vehicle.fee)

		else:
			pass_string = "Μη επαρκές ποσό"

			if isinstance(current_vehicle, Epivatiko):
				current_image = self.Epivatiko_nopass_image
			elif isinstance(current_vehicle, Dikyklo):
				current_image = self.Dikyklo_nopass_image
			else:
				current_image = self.Fortigo_nopass_image

			self.image_label.configure(image=current_image)
			self.update()

			current_epass.fortizei()

		self.attempted_passes += 1
		if self.attempted_passes >= 20:
			self.next_button.configure(state="disabled")
			self.results_button.configure(state="normal")

		self.stat_string.set(
			f'{current_epass.kwdkartas}\n'
			f'{current_vehicle.arKykloforias}\n'
			f'{current_vehicle.__class__.__name__}\n'
			f'{pass_string}')

	def to_results(self):
		self.destroy()
		self.parent.end_screen = EndScreen(self.parent)


class EndScreen(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.configure(bg="#FFFFFF")

		self.stat_frame = tk.Frame(self)

		tameio_stat_string = f"Συνολικές διελεύσεις: {tameio.arDieleysewn}\nΣυνολικά έσοδα: {tameio.esodaDieleysewn}€"

		self.tameio_stats = tk.Label(self.stat_frame, text=tameio_stat_string)
		self.tameio_stats.pack(side="left")

		car_stat_string = "Αρ. κυκλοφορίας/ Είδος οχηματος/\nΑρ. διελεύσεων/ Υπόλοιπο κάρτας\n"
		for vehicle in oximataList:
			if vehicle.arDieleysewn != 0:
				car_stat_string = car_stat_string + (
					f"{vehicle.arKykloforias}, "
					f"{vehicle.__class__.__name__}: "
					f"{vehicle.arDieleysewn}, "
					f"{vehicle.ePass.ypoloipoLogariasmou}\n"
				)

		self.car_stats = tk.Label(self.stat_frame, text=car_stat_string)
		self.car_stats.pack(side="left")

		# υπολογιζει αριθμο διελευσεων ανα ειδος οχηματος
		passes_list = [0, 0, 0]
		for oxima in oximataList:
			if isinstance(oxima, Epivatiko):
				passes_list[0] = passes_list[0] + oxima.arDieleysewn
			elif isinstance(oxima, Dikyklo):
				passes_list[1] = passes_list[1] + oxima.arDieleysewn
			elif isinstance(oxima, Fortigo):
				passes_list[2] = passes_list[2] + oxima.arDieleysewn

		self.graph1 = tk.Frame(self.stat_frame, background="white")
		self.graph_title = tk.Label(self.graph1, text="Διελεύσεις ανά\nείδος οχήματος", font=("Arial", 30))
		self.graph_title.pack()

		self.fig, self.ax = plt.subplots()
		self.ax.pie(passes_list, labels=["Επιβατικά", "Δίκυκλα", "Φορτηγά"], autopct="%1.1f%%")

		self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self.graph1)
		self.graph_canvas.get_tk_widget().pack()
		self.graph_canvas.draw()

		self.graph1.pack()

		self.stat_frame.pack()

		self.end_button = tk.Button(self, text="Τέλος", command=parent.quit)
		self.end_button.pack(side="top")

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
	['9977', 'NZK9955', 'Φορτηγό']
]

for i in range(len(vehiclesDict)):

	if vehiclesDict[i][2] == "Επιβατικό":
		oximataList.append(Epivatiko(vehiclesDict[i][1]))

	elif vehiclesDict[i][2] == "Δίκυκλο":
		oximataList.append(Dikyklo(vehiclesDict[i][1]))

	else:
		oximataList.append(Fortigo(vehiclesDict[i][1]))

	ePassList.append(Epass(vehiclesDict[i][0]))

# συνδεση οχηματος με εpass
	ePassList[-1].oxima = oximataList[-1]
	oximataList[-1].ePass = ePassList[-1]

app = App()
