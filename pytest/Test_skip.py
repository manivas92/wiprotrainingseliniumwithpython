#skip - if defects are there
#skip - if the testcases are absolute
#windows, mobile - OS dependency
import  pytest

def testcase1():
    print("Testcase 1 is executed")

@pytest.mark.skip
def testcase2():
    print("Testcase 2 is executed")

def test_case3():
    print("Testcase 3 is executed")

@pytest.mark.skip
def openbrowser():
    print("Opening the brower")
