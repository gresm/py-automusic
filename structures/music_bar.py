from __future__ import annotations

from . import AbstractBar, Configs, AbstractInstrument, AbstractNote, AbstractNotePromise


class MusicBar(AbstractBar):
    def __init__(self, configs: Configs, instrument: AbstractInstrument):
        self.configs = configs
        self.instrument = instrument
        self.notes: list[AbstractNote] = []

    def get_free_time(self) -> float:
        ret = self.configs.time_per_tact
        for note in self.notes:
            ret -= note.get_lasting_time()
        return ret

    def is_full(self) -> bool:
        return self.get_free_time() <= 0

    def add_note(self, note: AbstractNotePromise) -> bool:
        note = note.get_note(self)

        if self.get_free_time() - note.get_lasting_time() < 0:
            return False

        self.notes.append(note)
        return True
