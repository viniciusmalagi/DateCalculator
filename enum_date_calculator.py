from enum import Enum, auto

class DayOfWeek(Enum):
    SUNDAY = auto()
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()

class Months(Enum):
    JANUARY = auto()
    FEBRUARY = auto()
    MARCH = auto()
    APRIL = auto()
    MAY = auto()
    JUNE = auto()
    JULY = auto()
    AUGUST = auto()
    SEPTEMBER = auto()
    OCTOBER = auto()
    NOVEMBER = auto()
    DECEMBER = auto()

class KeyOfMonth(Enum):
    JANUARY = 1
    FEBRUARY = 4
    MARCH = 4
    APRIL = 0
    MAY = 2
    JUNE = 5
    JULY = 0
    AUGUST = 3
    SEPTEMBER = 6
    OCTOBER = 1
    NOVEMBER = 4
    DECEMBER = 6

class KeyOfWeek(Enum):
    SUNDAY = auto()
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = 0

YEAR_1900_TO_1999 = [
    [0, 6, 17, 23, 28, 34, 45, 51, 56, 62, 73, 79, 84, 90],
    [1, 7, 12, 18, 29, 35, 40, 46, 57, 63, 68, 74, 85, 91, 96],
    [2, 13, 19, 24, 30, 41, 47, 52, 58, 69, 75, 80, 86, 97],
    [3, 8, 14, 25, 31, 36, 42, 53, 59, 64, 70, 81, 87, 92, 98],
    [9, 15, 20, 26, 37, 43, 48, 54, 65, 71, 76, 82, 93, 99],
    [4, 10, 21, 27, 32, 38, 49, 55, 60, 66, 77, 83, 88, 94],
    [5, 11, 16, 22, 33, 39, 44, 50, 61, 67, 72, 78, 89, 95],
]
