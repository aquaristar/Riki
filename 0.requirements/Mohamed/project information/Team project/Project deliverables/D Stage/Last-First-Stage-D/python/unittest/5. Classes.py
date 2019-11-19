####################################################
# 5. Classes
####################################################

# We subclass from object to get a class.
class Human(object):
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self.age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age

import unittest

class TestClass(unittest.TestCase):
    def test_class(self):
        # Instantiate a class
        i = Human(name="Ian")
        self.assertTrue(i.say("hi"), )
        
        j = Human("Joel")
        self.assertTrue(j.say("hello"), )
        
        # Call our class method
        self.assertTrue(i.get_species(), )
        
        # Change the shared attribute
        Human.species = "H. neanderthalensis"
        self.assertTrue(i.get_species(), )
        self.assertTrue(j.get_species(), )
        
        # Call the static method
        self.assertTrue(Human.grunt(), )
        
        # Update the property
        i.age = 42
        
        # Get the property
        self.assertTrue(i.age, )
        
        # Delete the property
        del i.age
        try:
            i.age  # => raises an AttributeError
        except AttributeError:
            pass

if __name__ == '__main__':
    unittest.main()