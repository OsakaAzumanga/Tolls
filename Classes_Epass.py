import random


class Epass:
	def __init__(self, kwdkartas):
		self.kwdkartas = kwdkartas
		self.ypoloipoLogariasmou = round(random.uniform(0, 5), 2)
		self.oxima = None

	def fortizei(self):
		self.ypoloipoLogariasmou = round(random.uniform(0, 5), 2)

	def elegxei(self):
		if self.oxima.fee <= self.ypoloipoLogariasmou:
			return True
		else:
			return False

	def xrewnei(self):
		if self.oxima.fee <= self.ypoloipoLogariasmou:
			self.ypoloipoLogariasmou = round(self.ypoloipoLogariasmou - self.oxima.fee, 2)
			self.oxima.xrewnei()
		else:
			print("δεν υπαρχουν αρκετα λεφτα (καποιο λαθος στην main)")
