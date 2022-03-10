from . import AbstractBar

from abc import ABC, abstractmethod


class AbstractGenerator(ABC):
    @abstractmethod
    def generate_chunk(self) -> AbstractBar:
        pass

    def set_config(self, name: str, value) -> bool:
        pass


__all__ = [
    "AbstractGenerator"
]
