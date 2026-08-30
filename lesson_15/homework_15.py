# Homework 15.1

class GroupLimitError(Exception):
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}, "
            f"age: {self.age}, gender: {self.gender}"
        )


class Student(Human):

    def __init__(
        self,
        gender,
        age,
        first_name,
        last_name,
        record_book
    ):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"record book: {self.record_book}"
        )


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10 and student not in self.group:
            raise GroupLimitError(
                "В группе не может быть больше 10 студентов"
            )

        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)

        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self):
        all_students = ''

        for student in self.group:
            all_students += f"{student}\n"

        return f"Number: {self.number}\n{all_students}"


group = Group("PD1")

for number in range(1, 12):
    student = Student(
        "Male",
        20,
        f"Name{number}",
        f"Surname{number}",
        f"AN{number}"
    )

    try:
        group.add_student(student)
        print(f"Студент №{number} добавлен")
    except GroupLimitError as error:
        print(error)