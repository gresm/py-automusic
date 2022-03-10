from __future__ import annotations

from . import AbstractGenerator, AbstractInstrument, MusicBar, NotePromise, Note

import random as rd


class SimpleRandomGenerator(AbstractGenerator):
    def __init__(self, instrument: AbstractInstrument, max_detail: float, pitch_range: tuple[int, int]):
        self.instrument = instrument
        self.configs = self.instrument.configs
        self.max_detail = max_detail
        self.pitch_range = pitch_range

    def _beep_generate(self, value: float):
        if value <= self.max_detail:
            return value
        option = rd.randint(0, 3)
        if option == 0:
            return value
        elif option == 2:
            if value / 2 <= self.max_detail:
                return value
            v1 = self._beep_generate(value / 2)
            v2 = self._beep_generate(value / 2)

            if not isinstance(v1, list):
                v1 = [v1]

            if not isinstance(v2, list):
                v2 = [v2]

            return v1 + v2
        else:
            if value / 2 <= self.max_detail:
                return value
            v1 = self._beep_generate(value / 2)
            v2 = self._beep_generate(value / 2)

            if not isinstance(v1, list):
                v1 = [v1]

            if not isinstance(v2, list):
                v2 = [v2]

            return v2 + v1

    def _generate_beeps(self) -> list[float]:
        ret = self._beep_generate(self.configs.time_per_tact)

        if not isinstance(ret, list):
            return [ret]
        return ret

    def _generate_pitch(self):
        return rd.randint(0, self.pitch_range[1]) + self.pitch_range[0]

    def generate_chunk(self) -> MusicBar:
        bar = MusicBar(self.configs, self.instrument)
        for beep in self._generate_beeps():
            bar.add_note(NotePromise(Note, beep, octave=self._generate_pitch()))
        return bar


__all__ = [
    "SimpleRandomGenerator"
]
