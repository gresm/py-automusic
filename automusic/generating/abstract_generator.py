from . import AbstractBar

from abc import ABC, abstractmethod
from pydub import AudioSegment


class AbstractGenerator(ABC):
    @abstractmethod
    def generate_chunk(self) -> AbstractBar:
        pass

    def set_config(self, name: str, value) -> bool:
        pass

    def generate(self, chunks: int = 1) -> AudioSegment:
        assert chunks > 0

        gen = None
        for _ in range(chunks):
            if gen is None:
                gen = self.generate_chunk().generate()
            else:
                gen += self.generate_chunk().generate()
        assert gen is not None
        return gen


__all__ = [
    "AbstractGenerator"
]
