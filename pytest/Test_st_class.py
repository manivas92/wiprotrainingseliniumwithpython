# used inside the class
# it will run for every class definition 0nce  it will run starting and  at ending of the class

class Testclass1:

    def setup_class(cls):
        print("API Authorization needed with username and pasword")

    def teardown_class(cls):
        print("API Authorization closed")

    def testcase1(self):
        print("Testcase 1 is executed")

    def testcase2(self):
        print("Testcase 2 is executed")

    def test_case3(self):
        print("Testcase 3 is executed")

class Testclass2:

    def setup_class(cls):
        print("API Authorization needed with username and pasword")

    def teardown_class(cls):
        print("API Authorization closed")

    def testcase1(self):
        print("Testcase 1 is executed")

    def testcase2(self):
        print("Testcase 2 is executed")

    def test_case3(self):
        print("Testcase 3 is executed")
