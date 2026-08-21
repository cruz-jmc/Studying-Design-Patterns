from abc import ABC, abstractmethod


class DataLoader(ABC): # Target class (no modify)

    @abstractmethod
    def load(self) -> list[dict]:
        raise NotImplementedError