from __future__ import annotations

from pydub import AudioSegment, generators
from . import AbstractInstrument, AbstractNote, Note


class SinInstrument(AbstractInstrument):
    def _get_base_sound(self) -> AudioSegment:
        return generators.Sine(self.configs.starting_pitch).to_audio_segment(self.configs.note_speed)


class PauseNote(AbstractNote):
    time: int

    def __init__(self, instrument: AbstractInstrument, time: int):
        super(PauseNote, self).__init__(instrument)
        self.time = time

    def get_sound(self) -> AudioSegment:
        return AudioSegment.silent(self.time)

    def get_lasting_time(self) -> int:
        return self.time


class MultiNote(AbstractNote):
    time: int

    def __init__(self, instrument: AbstractInstrument, time: int, note: Note, notes: list[Note]):
        super(MultiNote, self).__init__(instrument)
        self.time = time
        self.note = note
        self.notes = notes

    def get_sound(self) -> AudioSegment:
        sound = self.note.get_sound()

        for note in self.notes:
            sound = sound.overlay(note.get_sound())

        return sound

    def get_lasting_time(self) -> int:
        return self.time


__all__ = [
    "SinInstrument",
    "PauseNote",
    "MultiNote"
]
