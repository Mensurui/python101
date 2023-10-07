from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic Bank: 0"
    
    @abstractmethod
    def withdraw(self, amount):
        pass

# Class Swiss
class Swiss(Bank):
    def __init__(self):
        self.bal = 1000  # Initialize the bank balance

    def basicinfo(self):
        bal_str = str(self.bal)
        print("This is the Swiss Bank")
        return "Swiss Bank: " + bal_str

    def withdraw(self, amount):
        self.amount = amount

        if amount > self.bal:
            print("Insufficient funds")
            return self.bal  # Return the original balance if insufficient funds
        else:
            self.bal -= self.amount  # Deduct the amount from the balance
            print("Withdrawn amount: " + str(amount))
            print("New balance: " + str(self.bal))
            return self.bal

def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()
