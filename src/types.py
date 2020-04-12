# WARNING: I'm not using any of these! Moved to pandas after I made this file...
from typing import NamedTuple, List, Tuple


class Restaurant(NamedTuple):
    code: str
    name: str
    max_breakfast: int
    max_lunch: int
    max_dinner: int
    max_days_per_week: int


Restaurants = [Restaurant]


class Hospital(NamedTuple):
    code: str
    name: str
    priority: int
    location: str
    zone: str
    orders: List[int]  # This should be 21 values long


Hospitals = [Hospital]


Assignment = Tuple[int, str]


class HospitalAssignment(NamedTuple):
    code: str
    name: str
    priority: int
    location: str
    zone: str
    orders: List[Assignment]  # This should be 21 values long


Results = [HospitalAssignment]
