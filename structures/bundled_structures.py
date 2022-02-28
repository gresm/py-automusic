from pydub import AudioSegment, generators
from . import AbstractInstrument


class SinInstrument(AbstractInstrument):
    def _get_base_sound(self) -> AudioSegment:
        return generators.Sine(self.configs.starting_pitch).to_audio_segment(self.configs.note_speed)


__all__ = [
    "SinInstrument"
]
