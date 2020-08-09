class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = str(name[0] + last_name + str(birth_year))


test = Student(input(),input(),input())
print(test.id)






