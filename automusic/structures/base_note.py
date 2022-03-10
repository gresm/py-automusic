from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Type

from pydub import AudioSegment

from . import AbstractInstrument, AbstractBar


class AbstractNote(ABC):
    time: float

    @abstractmethod
    def __init__(self, instrument: AbstractInstrument, time: float):
        self.instrument = instrument
        self.time = time

    @abstractmethod
    def get_sound(self) -> AudioSegment:
        pass

    @abstractmethod
    def get_lasting_time(self) -> int:
        pass


class AbstractNotePromise(ABC):
    time: float
    note_type: Type[AbstractNote]

    @abstractmethod
    def get_note(self, music_bar: AbstractBar) -> AbstractNote:
        pass


class NotePromise(AbstractNotePromise):
    def __init__(self, note_type: Type[AbstractNote], time: float = 1, **kwargs):
        self.time = time
        self.note_type = note_type
        self.kwargs = kwargs
        self.kwargs["time"] = self.time

    def get_note(self, music_bar: AbstractBar) -> AbstractNote:
        return self.note_type(music_bar.instrument, **self.kwargs)


class Note(AbstractNote):
    time: float
    octave: float

    def __init__(self, instrument: AbstractInstrument, time: float = 1, octave: float = 1):
        super(Note, self).__init__(instrument, time)
        self.octave = octave

    def get_sound(self) -> AudioSegment:
        return self.instrument.get_sound(self.octave, self.time)

    def get_lasting_time(self) -> float:
        return self.time


__all__ = [
    "AbstractNote",
    "AbstractNotePromise",
    "Note",
    "NotePromise"
]
