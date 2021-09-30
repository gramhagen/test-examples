from abc import ABC, abstractmethod


class BaseModel(ABC):

    @abstractmethod
    def __init__(self, path: str) -> None:
        pass

    @abstractmethod
    def predict(self, data: int) -> int:
        pass

