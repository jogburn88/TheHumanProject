import string
class Human(object):
    """ defines the basic human as a physical and mental being"""

    def __init__(self, name, sex):
        """ creates the simplest human possible
        name: takes a first name"""

        self._is_married = False
        self._name = str.capitalize(name)
        self._age = None
        self.set_sex(sex)

    def __str__(self):
        return "{} is a {}".format(self.get_first_name(), self.get_sex())

    def set_sex(self, sex):
        self._sex = sex

    def set_age(self, age):
        """sets the age of the person"""
        self._age = age

    def get_first_name(self):
        """returns the first name of the person"""
        return self._name

    def get_age(self):
        """gets the age of the person"""
        return self._age

    def get_sex(self):
        """returns the sex of the person"""
        return self._sex

    def switch_sex(self):
        print("Yeaaah, you can't really do this!")

    def get_is_married(self):
        return self._is_married


# class Sex(object):

class Female(Human):
    def __init__(self, name):
        super().__init__(name=name, sex="Female")



class Male(Human):

    def __init__(self, name):
        super().__init__(name=name, sex="Male")


x = Female("Rachel")
y = Female("Clara")
jesse = Male("Jesse")
print(jesse)