from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, hours):
        pass


class HourlyStrategy(PricingStrategy):
    def calculate_fee(self, hours):
        return hours * 5.0


class FlatRateStrategy(PricingStrategy):
    def calculate_fee(self, hours):
        return 10.0
