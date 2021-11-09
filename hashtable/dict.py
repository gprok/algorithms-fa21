

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        return self.name

def print_students(d):
    for key in d:
        print(d[key])


ht = {}
ht["Peter"] = Student("Peter", "CS")
ht["Mary"] = Student("Mary", "CS")
ht["John"] = Student("John", "IT")
ht["Nick"] = Student("Nick", "CS")
ht["Olga"] = Student("Olga", "CS")
ht["Tom"] = Student("Tom", "CS")

print_students(ht)

name = input("Give name: ")
st = ht[name]
if st is not None:
    print(name, " attends ", st.major)