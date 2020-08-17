class Student(object):
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def show_name(self):
        print(self.name, self.roll_number)


class Me(Student):

    def __init__(self, name, roll_number, marks):
        super(Me, self).__init__(name, roll_number)
        self.marks = marks

    def show_information(self):
        print("Name , roll number , marks ", self.name, self.roll_number, self.marks)


me = Me("Anshoo Mishra ", 14, 45)
me.show_information()
