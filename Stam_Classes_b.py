import random

class Oxima():
    """ Αυτή είναι η γονική κλάση όλων των οχημάτων"""
    def __init__(self,arKykloforias):
        self.arKykloforias=arKykloforias
        self.kwdkartas=kwdkartas #Αναφέρομαι στον κωδικό της εκάστοτε ePass
        self.ePass=None
class Epivatiko(Oxima):
    """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
    def __init__(self,arKykloforias):
        super().__init__(arKykloforias)
    
    def xrewnei(self):
        return 1.50 #Χρέωση διαφορετική σε κάθε όχημα για να υπολογίζεται το εκάστοτε κόστος διέλευσης

class Dikyklo(Oxima):
        """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
        def __init__(self,arKykloforias):
              super().__init__(arKykloforias)

        
        def xrewnei(self):
            return 0.60

class Fortigo(Oxima):
        """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
        def __init__(self,arKykloforias):
            super().__init__(arKykloforias)
        
        def xrewnei(self):
            return 3.20
    
class ePass():
    def __init__(self,kwdkartas,oxima,ypoloipoLogariasmou,arithmos_dieleysewn):
        self.kwdkartas=kwdkartas
        self.oxima=oxima
        self.ypoloipoLogariasmou=random.uniform(1,5)
        self.arithmos_dieleysewn=0
