from abc import ABC, abstractmethod
from pydub import AudioSegment


class BaseNote(ABC):
    time: float

    @abstractmethod
    def get_sound(self) -> AudioSegment:
        pass


# class Note(BaseNote):
#     time: float
#     pitch: float
#
#     def __init__(self, time: float, pitch: float):
#         self.time = time
#         self.pitch = pitch


__all__ = [
    "BaseNote"
]
