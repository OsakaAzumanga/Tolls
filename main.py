from testclasses import *
from Eleni_Classes import Bara, ePass

tameio = Tameios()
tollBar = Bara()
aisthitiras = Aisthitiras()



ePassList = []
oximataList = []


vehiclesDict = {
	'gr': [
		['1715', 'ΝΙΒ1000', 'Επιβατικό'], ['2230', 'ΝΚΚ2113', 'Δίκυκλο'],
		['3934', 'ΝΙΟ3225', 'Φορτηγό'], ['4141', 'PPE4789', 'Επιβατικό'],
		['5371', 'XAY5466', 'Επιβατικό'], ['6642', 'XIE6472', 'Επιβατικό'],
		['7499', 'NZT7228', 'Φορτηγό'], ['8107', 'NZK8331', 'Δίκυκλο'],
		['9503', 'NZK9112', 'Επιβατικό'], ['9977', 'NZK9955', 'Φορτηγό']
	],

	'uk': [['1715', 'ΝΙΒ1000', 'Car'], ['2230', 'ΝΚΚ2113', 'Motorcycle'],
		['3934', 'ΝΙΟ3225', 'Truck'], ['4141', 'PPE4789', 'Car'],
		['5371', 'XAY5466', 'Car'], ['6642', 'XIE6472', 'Car'],
		['7499', 'NZT7228', 'Truck'], ['8107', 'NZK8331', 'Motorcycle'],
		['9503', 'NZK9112', 'Car'], ['9977', 'NZK9955', 'Truck']
	]
}

for i in range(len(vehiclesDict["gr"])):

	if vehiclesDict["gr"][i][2] == "Επιβατικό":
		oximataList.append(Epivatiko(vehiclesDict["gr"][i][1], vehiclesDict["gr"][i][0]))

	elif vehiclesDict["gr"][i][2] == "Δίκυκλο":
		oximataList.append(Dikyklo(vehiclesDict["gr"][i][1], vehiclesDict["gr"][i][0]))

	else:
		oximataList.append(Fortigo(vehiclesDict["gr"][i][1], vehiclesDict["gr"][i][0]))

	ePassList.append(ePass(vehiclesDict["gr"][i][0], vehiclesDict["gr"][i][1]))

for i in range(20):
	current_epass = aisthitiras.anixneyei(ePassList) #(αυτο πρεπει να κανει return random ePass απο την λιστα)

	for j in oximataList:
		if j.arKykloforias == current_epass.arKykloforias:
			current_vehicle = j
			break




	# (η elegxei περνει Input ενα ποσο και βγαζει True αν η καρτα εχει >= λεφτα)
	if current_epass.elegxei(current_vehicle):

		current_epass.xrewnei(current_vehicle)
		tameio.addAxiaDieleysis()
		tollBar.anoigei()
		current_vehicle.dieleysei()

		tollBar.kleinei()
	else:
		print("δεν εχει λεφτα ξερωγω λολ")
		current_epass.fortizei()

print("διελευσεις:", tameio.arDieleysewn,"εσωδα",tameio.esodaDieleysewn )

for i in range(10):
	print("αριθμος κυκλοφοριας: ", oximataList[i].arKykloforias)
	print("αριθμος καρτας:", ePassList[i].kwdkartas,"    υποληπο καρτας", ePassList[i].ypoloipoLogariasmou)
	print("αριθμος διελευσεων", oximataList[i].arDieleysewn,"\n\n") #εδω υποθετω οτι εχουμε προσθεσει μια μεταβλητη arDieleysewn στα οχηματα για να μετραμε τις διελευσεις που εχει κανει καθε οχημα
