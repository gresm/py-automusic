from abc import ABC, abstractmethod
from pydub import AudioSegment


class AbstractNote(ABC):
    time: float

    @abstractmethod
    def get_sound(self) -> AudioSegment:
        pass


__all__ = [
    "AbstractNote"
]
