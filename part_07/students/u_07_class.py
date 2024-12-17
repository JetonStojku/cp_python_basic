from dataclasses import dataclass


@dataclass
class Student:
    country: str
    first_name: str
    last_name: str
    age: int
    score: [int]
    gender: str

    def total_score(self):
        return sum(self.score)

    def avg(self):
        return self.total_score() / len(self.score)
