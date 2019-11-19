####################################################
#  3. Control Flow
####################################################

import unittest

class TestControlFlow(unittest.TestCase):

    def test_comparison(self):
        # Let's just make a variable
        some_var = 15
    
        # Here is an if statement. Indentation is significant in python!
        # prints "some_var is smaller than 10"
        if some_var > 10:
            str = "some_var is totally bigger than 10."
        elif some_var < 10:  # This elif clause is optional.
            str =  "some_var is smaller than 10."
        else:  # This is optional too. (smoe_var == 10)
            str =  "some_var is indeed 10."
        
        self.assertEqual(str, )
    
    def test_loop(self):
        """
        For loops iterate over lists
        prints:
            dog is a mammal
            cat is a mammal
            mouse is a mammal
        """
        s = ""
        for animal in ["dog", "cat", "mouse"]:
            # You can use {0} to interpolate formatted strings. (See above.)
            s += "{0} is a mammal ".format(animal)
    
        self.assertEqual(s, )
        
        """
        "range(number)" returns a list of numbers
        from zero to the given number
        """
        s = ""
        for i in range(4):
            s += "{0} ".format(i)
        self.assertEqual(s, )
         
        """
        "range(lower, upper)" returns a list of numbers
        from the lower number to the upper number
        """
        s = ""
        for i in range(4, 8):
            s += "{0} ".format(i)
        self.assertEqual(s, )
        
        """
        While loops go until a condition is no longer met.
        prints:
            0
            1
            2
            3
        """
        x = 0
        while x < 4:
            x += 1  # Shorthand for x = x + 1
        self.assertEqual(x, 4)
        # Handle exceptions with a try/except block
        
        # Works on Python 2.6 and up:
        try:
            # Use "raise" to raise an error
            raise IndexError("This is an index error")
        except IndexError as e:
            pass  # Pass is just a no-op. Usually you would do recovery here.
        except (TypeError, NameError):
            pass  # Multiple exceptions can be handled together, if required.
        else:  # Optional clause to the try/except block. Must follow all except blocks
            print "All good!"  # Runs only if the code in try raises no exceptions
        finally:  # Execute under all circumstances
            print "We can clean up resources here"
        
        # Instead of try/finally to cleanup resources you can use a with statement
        with open("test.txt") as f:
            s = ""
            for line in f:
                s += line
        self.assertEqual(s, "hello1\nhello2")

if __name__ == '__main__':
    unittest.main()