from abc import ABC, abstractmethod

class Bank(ABC):
    def basic_info():
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw():
        pass

class Swiss(Bank):
    def __init__(self):
        super().__init__()
        self.bal = 1000

    def basic_info(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)
    
    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal >= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New Balance: {self.bal}")
            return self.bal
        else:
            print("Insufficient funds")
            return self.bal

def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basic_info())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()