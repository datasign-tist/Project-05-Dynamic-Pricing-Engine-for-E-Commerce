from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def get_price(self, input_data):
        pass
