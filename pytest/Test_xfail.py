#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import pytest

@pytest.mark.xfail(reason = "known bug in the third-party library")
def test_function_with_bug():
    assert (1+1)==3

@pytest.mark.sanity
def testcase1():
    print("Testcase 1 is executed")

@pytest.mark.regression
def testcase2():
    print("Testcase 2 is executed")

@pytest.mark.db
def test_case3():
    print("Testcase 3 is executed")