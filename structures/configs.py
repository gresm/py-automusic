from dataclasses import dataclass


@dataclass
class Configs:
    notes_per_tact: int
    note_speed: int
    starting_pitch: int


def default_configs():
    return Configs(notes_per_tact=4, note_speed=1000, starting_pitch=200)


__all__ = [
    "Configs",
    "default_configs"
]
