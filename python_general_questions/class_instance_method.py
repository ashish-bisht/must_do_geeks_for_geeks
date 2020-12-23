from datetime import date


class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    @classmethod
    def create_with_date_of_birth(cls, first_name, second_name, year):
        return cls(first_name, second_name, date.today().year - year)

    # dont belong to any instance, dont have power to change class variable

    @staticmethod
    def is_adult(age):
        return age > 18


# POerson created with default constructor
print("#################### Cretead by Default ####################")
person1 = Person("ash", "bisht", 27)
print(person1.first_name)
print(person1.age)


print("#################### Cretead by Factory ####################")
person2 = Person.create_with_date_of_birth("ash", "bisht", 1992)
print(person2.first_name)
print(person2.age)
