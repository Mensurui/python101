class Employees :
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
    
class Supervisor(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chefs(Employees):
    def leave_request(self, days):
        return "May I have a leave for: " + str(days) + " days"
    
Mensur = Supervisor("Mensur" , "K", "Mensur")
Imran = Chefs("Imran" , "K")
Nejma = Chefs("Nejma" , "K")

print(Imran.leave_request(5))
print(Mensur.password)

Mensur.password = "password"
print(Mensur.password)
print(Nejma.name)
        