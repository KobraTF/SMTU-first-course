class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)
class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)

class Person:
    def __init__(self, name, surname, number, learner:Learner=None, teacher:Teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher
    def enrol(self, course):
        try:
             self.learner.enrol(course)
        except:
            print('This person is not learner')
    def assign_teaching(self,course):
        try:
             self.teacher.assign_teaching(course)
        except:
            print('This person is not teacher')

jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.enrol('a_postgrad_course')
jane.assign_teaching('an_undergrad_course')
