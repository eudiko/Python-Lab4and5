from abc import ABC, abstractmethod

class Supporter(ABC):
    @abstractmethod
    def give_rewards(self):
        pass

class MonetarySupporter(Supporter):
    def give_rewards(self):
        print("Giving rewards as financial support through donations or subscriptions.")

class MerchandiseSupporter(Supporter):
    def give_rewards(self):
        print("Giving rewards through the purchase of branded merchandise.")

class ExclusiveContentSupporter(Supporter):
    def give_rewards(self):
        print("Giving rewards by accessing exclusive content for subscribers.")

supporters = [
    MonetarySupporter(),
    MerchandiseSupporter(),
    ExclusiveContentSupporter()
]

for supporter in supporters:
    supporter.give_rewards()
