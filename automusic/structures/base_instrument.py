from abc import ABC, abstractmethod
from pydub import AudioSegment

from .configs import Configs


class AbstractInstrument(ABC):
    def __init__(self, configs: Configs):
        self.configs = configs

    @abstractmethod
    def _get_base_sound(self) -> AudioSegment:
        pass

    def _get_partial_sound(self, octaves: float) -> AudioSegment:
        sound = self._get_base_sound()
        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
        # noinspection PyProtectedMember
        return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

    def get_sound(self, octaves: float, sound_length: float):
        sound = self._get_partial_sound(octaves)
        missing = self.configs.note_speed / len(sound)
        return sound * int(missing * sound_length)


__all__ = [
    "AbstractInstrument"
]
