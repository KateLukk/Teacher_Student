class Human:
    def __init__(self, name, age, city, sex, id):
        self.name = name
        self.age = age
        self.city = city
        self.sex = sex
        self.id = id


class Teacher(Human):
    def __init__(self, name, age, city, workplace, marital_status, sex, id):
        super().__init__(name, age, city, sex, id)
        self.workplace = workplace
        self.marital_status = marital_status

    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.id == other.id
        return False

    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\nid: " + str(self.id)

    def fired(self):
        self.workplace = None


class Student(Human):
    def __init__(self, name, age, city, sex, id, hobby, school):
        super().__init__(name, age, city, sex, id)
        self.hobby = hobby
        self.school = school

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id
        return False

    def __str__(self):
        return "Name:" + self.name + "Age:" + str(self.age) + "id:" + self.id


T1 = Teacher('a', 21, 's', 't', 's', 'f', 1205)
T2 = Teacher('y', 23, 'm', 'z', 'd', 'm', 1205)
S1 = Student('k', 12, 'm', 'f', 9899, 'k', 22)
S2 = Student('k', 12, 'm', 'f', 9899, 'k', 22)

print(S2 == S1)

