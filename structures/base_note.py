from pydub import AudioSegment

from . import AbstractInstrument


class BaseNote:
    time: int
    octave: float

    def __init__(self, instrument: AbstractInstrument, octave: float = 1, time: int = 1):
        self.instrument = instrument
        self.time = time
        self.octave = octave

    def get_sound(self) -> AudioSegment:
        return self.instrument.get_sound(self.octave, self.time)


__all__ = [
    "BaseNote"
]
