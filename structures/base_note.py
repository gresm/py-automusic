from abc import ABC, abstractmethod
from pydub import AudioSegment

from . import AbstractInstrument


class AbstractNote(ABC):
    @abstractmethod
    def __init__(self, instrument: AbstractInstrument):
        self.instrument = instrument

    @abstractmethod
    def get_sound(self) -> AudioSegment:
        pass

    @abstractmethod
    def get_lasting_time(self) -> int:
        pass


class Note(AbstractNote):
    time: int
    octave: float

    def __init__(self, instrument: AbstractInstrument, octave: float = 1, time: int = 1):
        super(Note, self).__init__(instrument)
        self.time = time
        self.octave = octave

    def get_sound(self) -> AudioSegment:
        return self.instrument.get_sound(self.octave, self.time)

    def get_lasting_time(self) -> int:
        return self.time


__all__ = [
    "AbstractNote",
    "Note"
]
