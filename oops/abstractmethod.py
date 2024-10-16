"""from abc import ABC ,abstractmethod

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        pass
    #sub class/child class of abstract class

class SBI(bank):
    def interest(self):
        print("5 percentage")

s=SBI()
s.bank_info()
s.interest()"""

"""from abc import ABC ,abstractmethod

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        pass
    #sub class/child class of abstract class

class SBI(bank):
    def interest(self):
        print("hi")
    def balance(self):
        print("balance is 2121")

s=SBI()
s.bank_info()
s.balance()
s.interest()"""

from abc import ABC ,abstractmethod

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def balance(self):
        pass
    #sub class/child class of abstract class

class SBI(bank):
    def balance(self):
        print("balance is 2121")
class sub(SBI):
    def interest(self):
        print("5")
s=sub()
s.bank_info()
s.balance()
s.interest()