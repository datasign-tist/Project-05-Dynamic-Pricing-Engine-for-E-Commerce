from abc import ABC, abstractmethod

class ModelTrainer(ABC):
    @abstractmethod
    def train(self, X, y):
        pass

    @abstractmethod
    def evaluate(self, X, y):
        pass
