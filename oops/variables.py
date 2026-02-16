class student:

    school = "sanskriti vidyalaya"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show(self):
        schoolcity = "Darsi"
        print(self.marks, self.name)
        print(schoolcity)
        print(self.school)

s1 = student("Manivas",95)
s2 = student("sai",83)

s1.show()
s2.show()