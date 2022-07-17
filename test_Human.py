import unittest as ut
from Human import Human
from unittest import TestCase


class Testing(ut.TestCase):
    def test_string(self):
        a = "some"
        b = "some"

        self.assertEqual(a, b)


class TestHuman(ut.TestCase):
    human = Human("John", "Male")
    test_name = "john"
    test_sex = "Male"
    test_get_is_married = False

    def test_Human_print_string(self):
        print("Begin testing the Human class \n")
        print("Test if printing a human instance returns the name of the human")
        #self.assertEqual(self.human.__str__(), self.test_name)

        try:
            self.assertEqual(self.human.get_first_name(), self.test_name)
        except AssertionError:
            print("\n get_first_name did not pass the test.")
            print(e)

        self.assertEqual(self.human.get_sex(), self.test_sex)
        self.assertEqual(self.human.get_is_married(), self.test_get_is_married, "is_married did not pass")

if __name__ == '__main__':
    # begin the unittest.main()
    ut.main()
