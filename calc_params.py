from dataclasses import dataclass


@dataclass
class CalcParameters:
    first_number: float
    second_number: float
    operation: str