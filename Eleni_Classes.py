import random


class Epass:
	def __init__(self, kwdkartas):
		self.kwdkartas = kwdkartas
		self.ypoloipoLogariasmou = random.uniform(0, 5)
		self.oxima = None

	def fortizei(self):
		self.ypoloipoLogariasmou = random.uniform(0, 5)

	def elegxei(self):
		if self.oxima.poso <= self.ypoloipoLogariasmou:
			return True
		else:
			return False

	def xrewnei(self):
		if self.oxima.poso <= self.ypoloipoLogariasmou:
			self.ypoloipoLogariasmou -= self.oxima.poso
		else:
			print("δεν υπαρχουν αρκετα λεφτα (καποιο λαθος στην main)")
