class student:

    studentName = "manivas"
    studentID = "20061"
    mobileno = "9666666666"
    def displaystudentdetails(self):
        print(self.studentName)
        print(self.studentID)
        print(self.mobileno)

a = student()
a.displaystudentdetails()


class employee1:
     empID = "92092"
     empName ="Manivas"
     empDep = "CSE"

class employee2:
    empID = "92093"
    empName = "hemanth"
    empDep = "ECE"

    def displayemployedetails(self):
        print(self.empId)
        print(self.empName)
        print(self.empDep)

a = employee1(), employee2()
a.displayemployedetails()