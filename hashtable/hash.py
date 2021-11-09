
# Convert string s to a number up to b
def hash_function(s, b):
    total = 0
    for c in s:
        total += ord(c)
    return total % b


class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        return self.name


class HasTable:
    def __init__(self):
        self.table = [[], [], [], [], [], [], [], [], [], []]

    def add_student(self, student):
        index = hash_function(student.name, 10)
        print(index)
        self.table[index].append(student)

    def display(self):
        for list in self.table:
            print('[', end=' ')
            for s in list:
                print(s, end=", ")
            print(']')

    def find_student(self, name):
        student = None
        index = hash_function(name, 10)
        list = self.table[index]
        for s in list:
            if s.name == name:
                student = s
                break
        return student


ht = HasTable()
ht.add_student(Student("Peter", "CS"))
ht.add_student(Student("Mary", "CS"))
ht.add_student(Student("John", "IT"))
ht.add_student(Student("Nick", "CS"))
ht.add_student(Student("Olga", "CS"))
ht.add_student(Student("Tom", "CS"))

ht.display()

name = input("Give name: ")
st = ht.find_student(name)
if st is not None:
    print(name, " attends ", st.major)


