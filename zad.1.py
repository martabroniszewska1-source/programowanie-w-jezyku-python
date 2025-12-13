class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if not self.marks:
            return False

        average = sum(self.marks) / len(self.marks)
        return average > 50


student_passed = Student("Anna Kowalska", [60, 70, 80])
student_failed = Student("Piotr Nowak", [30, 40, 50])

print(f"Czy student {student_passed.name} zdał? {student_passed.is_passed()}")
print(f"Czy student {student_failed.name} zdał? {student_failed.is_passed()}")
