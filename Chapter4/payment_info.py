class Payement_Slip:
    def __init__(self, payment, amount, name) -> None:
        self.payment = payment
        self.amount = amount
        self.name = name
        
    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes" :
            print("Payment successful from " + self.name + " of amount: " + self.amount)
        else:
            print("Payment failed from " + self.name + " of amount: " + self.amount)
    
    

nathan = Payement_Slip("no", "2000$", "Nathan")
mensur = Payement_Slip("yes", "2000$", "Mensur")
print("_____________________________________________________________")
nathan.status()
print("---------------------------------------------------------------")
mensur.status()
print("_____________________________________________________________")
 
    