# Association
class Teacher:
    pass

class Student:
    def __init__(self, teacher: Teacher):
        self.teacher = teacher

# (Test)
maam_mona = Teacher()
client = Student(maam_mona)
print(client.teacher is maam_mona)
