from dataclasses import dataclass


@dataclass
class Configs:
    time_per_tact: float
    note_speed: int
    starting_pitch: int
    pitch_detail: float


def default_configs():
    return Configs(time_per_tact=8, note_speed=1000, starting_pitch=150, pitch_detail=0.5)


__all__ = [
    "Configs",
    "default_configs"
]
