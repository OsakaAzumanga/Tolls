import random


class Bara:

	def __init__(self):
		self.anoixti = False

	def anoigei(self):
		if not self.anoixti:
			self.anoixti = True
			print("Η μπάρα ανοίγει")
		else:
			print("Η μπάρα είναι ηδη ανοιχτη")

	def kleinei(self):
		if self.anoixti:
			self.anoixti = False
			print("η μπάρα κλείνει")
		else:
			print("Η μπάρα είναι ηδη κλειστή")

			
class ePass:
	def __init__(self, kwdkartas):
		self.kwdkartas = kwdkartas
		self.ypoloipoLogariasmou = random.uniform(0, 5)
		self.oxima = None

	def fortizei(self):
		self.ypoloipoLogariasmou = random.uniform(0, 5)

	def elegxei(self, vehicle):
		if vehicle.poso <= self.ypoloipoLogariasmou:
			return True
		else:
			return False

	def xrewnei(self, vehicle):
		if(vehicle.poso <= self.ypoloipoLogariasmou):
			self.ypoloipoLogariasmou -= vehicle.poso
		else:
			print("δεν υπαρχουν αρκετα λεφτα (καποιο λαθος στην main)")

