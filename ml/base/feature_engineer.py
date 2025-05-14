from abc import ABC, abstractmethod

class FeatureEngineer(ABC):
    @abstractmethod
    def transform(self, data):
        pass
