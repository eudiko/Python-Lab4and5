from abc import ABC, abstractmethod

class Supporter(ABC):
    @abstractmethod
    def support(self):
        pass

class Donor(Supporter):
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    def support(self):
        print(f"{self.name} has donated {self.amount} $ towards the project")

class Subscriber(Supporter):
    def __init__(self,name,months):
        self.name = name
        self.months = months
    def support(self):
        print(f"{self.name} has subscribed for {self.months} months")

class Funder(Supporter):
    def __init__(self,name,funds):
        self.name = name
        self.funds = funds
    def support(self):
        print(f"{self.name} has funded the project with {self.funds} $")
    

_donor = Donor(name = "Sam",amount=40)
_subscriber = Subscriber(name = "Jeff",months=5)
_funder = Funder(name = "Charlie", funds=5000)

supporter_all = [_donor, _subscriber, _funder]

for _supporter in supporter_all:
    _supporter.support() 
