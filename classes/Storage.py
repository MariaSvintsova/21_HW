from abc import ABC, abstractmethod

"""Абстрактный родительский класс со всеми главными методами"""
class Storage(ABC):

    @abstractmethod
    def __init__(self, items, capacity) -> None:
        self.items: dict[str, int] = items
        self._capacity: int = capacity

    @abstractmethod
    def add(self, item: str, capacity: int) -> None:
        pass

    @abstractmethod
    def remove(self, item: str, capacity: int):
        pass

    @abstractmethod
    def get_free_space(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass

