from unittest.mock import patch
import unittest
from unittest.mock import Mock

class MyClass:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        return "hi my name is: {}".format(self.name)

# instantiates MyClass and calls a method on the object
def function_b():
    param1 = MyClass("foo")

    # returns "hi my name is: foo"
    return param1.sayhi()


def test_function_b():

    # mock an object of class
    with patch.object(MyClass, 'sayhi', return_value="hi i'm a mock object"):

        # the MyClass object used within function_b will
        # be replaced by a mock defined in the
        # patch.object call above
        assert function_b() == "hi i'm a mock object"

if __name__ == "__main__":
    unittest.main()

 mock = Mock()
 mock.