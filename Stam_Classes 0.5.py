import random

class Oxima():
    """ Αυτή είναι η γονική κλάση όλων των οχημάτων"""
    def __init__(self,arKykloforias,eidos_oximatos,kwdkartas)
    self.arKykloforias=arKykloforias
    self.eidos_oximatos=eidos_oximatos #το είδος οχήματος κληρονομείται σε όλες τις υποκλάσεις για αυτό το κρατάω στην γονική - είναι κοινό χαρακτηριστικό όλων των οχημάτων#
    self.kwdkartas=kwdkartas #Αναφέρομαι στον κωδικό της εκάστοτε ePass
class Epivatiko(Oxima):
    """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
    def __init__(self,arKykloforias,eidos_oximatos,kwdkartas)

    def xrewnei(self):
        return 1.50 #Χρέωση διαφορετική σε κάθε όχημα για να υπολογίζεται το εκάστοτε κόστος διέλευσης

class dikyklo(Oxima):
        """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
    def __init__(self,arKykloforias,eidos_oximatos,kwdkartas)

    def xrewnei(self):
        return 0.60

class Fortigo(Oxima):
        """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
    def __init__(self,arKykloforias,eidos_oximatos,kwdkartas)
    def xrewnei(self):
        return 3.20
    
class ePass():
    def __init__(self,kwdkartas,oxima,ypoloipoLogariasmou,arithmos_dieleysewn)
    self.kwdkartas=kwdkartas
    self.oxima=oxima
    self.ypoloipoLogariasmou=random.uniform(1,5)
    self.arithmos_dieleysewn=0
