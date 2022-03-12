from __future__ import annotations

from ..structures import AbstractBar

from abc import ABC, abstractmethod
from pydub import AudioSegment


class AbstractGenerator(ABC):
    @abstractmethod
    def generate_chunk(self) -> AbstractBar:
        pass

    @classmethod
    def list_to_audio(cls, converting: list[AbstractBar]) -> AudioSegment:
        assert len(converting) > 0
        a = None
        for el in converting:
            if a is None:
                a = el.generate()
            else:
                a += el.generate()
        return a

    def set_config(self, name: str, value) -> bool:
        pass

    def generate_list(self, chunks: int = 1) -> list[AbstractBar]:
        assert chunks > 0
        gen = []
        for _ in range(chunks):
            gen.append(self.generate_chunk())
        return gen

    def generate(self, chunks: int = 1) -> AudioSegment:
        assert chunks > 0
        return self.list_to_audio(self.generate_list(chunks))


__all__ = [
    "AbstractGenerator"
]
