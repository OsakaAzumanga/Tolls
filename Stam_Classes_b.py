
class Oxima():
    """ Αυτή είναι η γονική κλάση όλων των οχημάτων"""
    def __init__(self,arKykloforias):
        self.arKykloforias=arKykloforias
        self.ePass=None
        self.arDieleysewn = 0
class Epivatiko(Oxima):
    """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
    def __init__(self,arKykloforias):
        super().__init__(arKykloforias)
        self.fee = 1.50#Χρέωση διαφορετική σε κάθε όχημα για να υπολογίζεται το εκάστοτε κόστος διέλευσης
    
    def xrewnei(self):
        self.arDieleysewn+=1

class Dikyklo(Oxima):
        """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
        def __init__(self,arKykloforias):
            super().__init__(arKykloforias)
            self.fee = 0.60
        
        def xrewnei(self):
            self.arDieleysewn += 1

class Fortigo(Oxima):
        """Αυτή η κλάση κληρονομεί όλα τα χαρακτηριστικά της γονικής με την προσθήκη της εξειδικευμένης χρέωσης που απαντάνται μόνο σε αυτήν"""
        def __init__(self,arKykloforias):
            super().__init__(arKykloforias)
            self.fee = 3.20
        def xrewnei(self):
            self.arDieleysewn += 1
