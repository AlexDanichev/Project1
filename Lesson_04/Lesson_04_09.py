from abc import ABC, abstractmethod
import datetime

class Person(ABC):

    @abstractmethod
    def say_name(self):
        print(self._name)

    def say_faculty(self):
        print(self._faculty)

    def say_age(self):
        birthDate = self._age
        today = datetime.date.today()
        age_today = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        print(age_today)

    @abstractmethod
    def say_all(self):
        print(self._name)
        print(self._faculty)
        birthDate = self._age
        today = datetime.date.today()
        age_today = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        print(age_today)

class Teacher(Person):

    def __init__(self, name, faculty, age):
        self._name = name
        self._faculty = faculty
        self._age = age

    def say_name(self):
        super().say_name()

    def say_faculty(self):
        super().say_faculty()

    def say_age(self):
        super().say_age()
    def say_all(self):
        super().say_all()

misha = Teacher ("misha", "KPU", datetime.date( 1991, 6, 3 ) )
misha.say_name()
misha.say_faculty()
misha.say_all()