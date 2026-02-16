# module level - runs once per module (file)
# use module level set up and tear down when you want to
# execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection
#setup_module - -> only one per file
#set_class() -> one per class
#set_method() -> one per file
#set_function() -> one per file

import pytest

def setup_module(module):
    print("opening the db connection")

def teardown_module(module):
    print("closing the db connection")


def test_read():
    print("Reading the db")

def test_write():
    print("writing the data to db")

@pytest.mark.regression
def test_updating():
    print("updating the data to db")


