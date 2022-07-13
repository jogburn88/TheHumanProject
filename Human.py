import string

class Human(object):
    """ defines the basic human as a physical and mental being"""

    def __init__(self, name):
        """ creates the simplest human possible
        name: takes a first name"""

        self.name = str.capitalize(name)

    def get_first_name(self):
        return self.name

