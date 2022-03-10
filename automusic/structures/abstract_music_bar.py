from abc import ABC, abstractmethod

from pydub import AudioSegment

from . import Configs, AbstractInstrument


class AbstractBar(ABC):
    configs: Configs
    instrument: AbstractInstrument

    @abstractmethod
    def get_free_time(self) -> float:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def add_note(self, note) -> bool:
        pass

    @abstractmethod
    def generate(self) -> AudioSegment:
        pass


__all__ = [
    "AbstractBar"
]
