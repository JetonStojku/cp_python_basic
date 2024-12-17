from dataclasses import dataclass


@dataclass
class Student:
    country: str
    first_name: str
    last_name: str
    age: int
    grade: int
    gender: str
