from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def donate(self):
        pass
    
class Donation(Employee):
    def donate(self):
        a= input("How much do you want to donate: ")
        return a
    
class DonationHigher(Employee):
    def donate(self):
        Dh = input("Do you want to contribute to the donation if so how much do you want to contribute: ")
        return Dh

staus = input("what is your status A for employee B for Higher Office Stuff: ")

if staus == "A":
    amounts = []
    jhon = Donation()
    j = jhon.donate()
    amounts.append(j)

    mary = Donation()
    m = mary.donate()
    amounts.append(m)

    print(amounts)
elif staus == "B":
    vicePresidents = []

    mensur = DonationHigher()
    me = mensur.donate()
    vicePresidents.append(me)
    print(vicePresidents)
else:
    print("Please choose the correct status")