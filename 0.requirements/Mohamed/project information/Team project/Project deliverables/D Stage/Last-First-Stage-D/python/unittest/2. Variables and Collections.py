####################################################
# 2. Variables and Collections
####################################################

import unittest

class TestVariablesAndCollections(unittest.TestCase):

    def test_string(self):
        s = "I'm Python. Nice to meet you!"
        s1 = "I'm Python." + " Nice to meet you!"
        # Python is smart to understand the meaning of sameness in string
        self.assertTrue("I'm Python. Nice to meet you!" == s)
        self.assertTrue("I'm Python. Nice to meet you!" == s1)
        self.assertFalse(id(s) == id(s1))

    def test_variable(self):
        # No need to declare variables before assigning to them.
        some_var = 5  # Convention is to use lower_case_with_underscores
        self.assertEqual(some_var, )

        # Accessing a previously unassigned variable is an exception.
        # See Control Flow to learn more about exception handling.

        try:
            some_other_var  # Raises a name error
        except Exception:
            pass 

        # if can be used as an expression
        # Equivalent of C's '?:' ternary operator
        self.assertEqual(("yahoo" if 3 > 2 else "yaho"), )  

    def test_list(self):
        # Lists store sequences
        li = []
    
        # Add stuff to the end of a list with append
        li.append(1)  # li is now [1]
        li.append(2)  # li is now [1, 2]
        li.append(4)  # li is now [1, 2, 4]
        li.append(3)  # li is now [1, 2, 4, 3]
        self.assertTrue(li == )
        
        # Remove from the end with pop
        li.pop()  # => 3 and li is now [1, 2, 4]
        self.assertTrue(li == )
        # Let's put it back
        li.append(3)  # li is now [1, 2, 4, 3] again.
        self.assertTrue(li == )
        
        # Access a list like you would any array
        self.assertEqual(li[0], )
        # Assign new values to indexes that have already been initialized with =
        li[0] = 42
        self.assertEqual(li[0], )

        li[-1] = 30 # last value is assigned to 30
        self.assertTrue(li == )

        # Looking out of bounds is an IndexError
        try:
            li[4]  # Raises an IndexError
        except IndexError:
            pass

        li = [1,2,4,3]
        # You can look at ranges with slice syntax.
        # (It's a closed/open range for you mathy types.)
        self.assertEqual(li[1:3],)
        # Omit the beginning
        self.assertEqual(li[2:], )
        # # Omit the end
        self.assertEqual(li[:3], )
        # Select every second entry
        self.assertEqual(li[::2], )
        # Reverse a copy of the list
        self.assertEqual(li[::-1], )
        # Use any combination of these to make advanced slices
        # li[start:end:step]
        li = [0,1,2,3,4,5,6,7,8]
        self.assertEqual(li[0:5:2], )
        #Remove arbitrary elements from a list with "del"
        del li[0]  
        self.assertEqual(li, )

        # You can start with a prefilled list
        li = [1,2,3]
        other_li = [4, 5, 6]
        # You can add lists
        self.assertEqual(li + other_li, )
        # Note: values for li and for other_li are not modified.
        #
        # Concatenate lists with "extend()"
        li.extend(other_li)
        # They have the same values
        self.assertEqual(li, )
        # They are different objects
        self.assertTrue(id(li) != id([1, 2, 3, 4, 5, 6]))
        #
        # Remove first occurrence of a value
        li.remove(2)  # li is now [1, 3, 4, 5, 6]
        self.assertEqual(li, )
        try:
            li.remove(2)  # Raises a ValueError as 2 is not in the list
        except ValueError:
            pass
        #
        # Insert an element at a specific index
        li.insert(1, 2)  # li is now [1, 2, 3, 4, 5, 6] again
        self.assertEqual(li, )
        #
        # Get the index of the first item found
        self.assertEqual(li.index(2), )
        try:
            li.index(7)  # Raises a ValueError as 7 is not in the list
        except ValueError:
            pass
        #
        # Check for existence in a list with "in"
        self.assertEqual(1 in li, )
        #
        # Examine the length with "len()"
        self.assertEqual(len(li), )

    def test_tuple(self):
        # Tuples are like lists but are immutable.
        tup = (1, 2, 3)
        self.assertEqual(tup[0], )
        try:
            tup[0] = 3  # Raises a TypeError
        except TypeError:
            pass

        # You can do all those list thingies on tuples too
        self.assertEqual(len(tup),  )
        self.assertEqual(tup + (4, 5, 6), )
        self.assertEqual(tup[:2], )
        self.assertEqual(2 in tup, )
        #
        # You can unpack tuples (or lists) into variables
        a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
        self.assertTrue(a ==  and b == 2 and c == 3)
        d, e, f = 4, 5, 6  # you can leave out the parentheses
        self.assertTrue(d ==  and e == 5 and f == 6)
        # Tuples are created by default if you leave out the parentheses
        g = 4, 5, 6  # => (4, 5, 6)
        self.assertEqual(g[0], )
        # Now look how easy it is to swap two values
        e, d = d, e  # d is now 5 and e is now 4
        self.assertTrue(e ==  and d == 5)
        
    def test_dict(self):
        # Dictionaries store mappings
        empty_dict = {}
        # Here is a prefilled dictionary
        filled_dict = {"one": 1, "two": 2, "three": 3}
        # Look up values with []
        self.assertEqual(filled_dict["one"], )
        #
        # Get all keys as a list with "keys()"
        self.assertEqual(filled_dict.keys(), )
        # Note - Dictionary key ordering is not guaranteed.
        # Your results might not match this exactly.
        
        # Get all values as a list with "values()"
        self.assertEqual(filled_dict.values(), )
        # Note - Same as above regarding key ordering.
        #
        # Get all key-value pairs as a list of tuples with "items()"
        self.assertEqual(filled_dict.items(), )
        #
        # Check for existence of keys in a dictionary with "in"
        self.assertEqual("one" in filled_dict, )
        self.assertEqual(1 in filled_dict, )
        #
        # Looking up a non-existing key is a KeyError
        try:
            filled_dict["four"]  
        except KeyError:
            pass
            #
        # Use "get()" method to avoid the KeyError
        self.assertEqual(filled_dict.get("one"), )
        self.assertEqual(filled_dict.get("four"), )  # => None
        # The get method supports a default argument when the value is missing
        self.assertEqual(filled_dict.get("one", 4), )
        self.assertEqual(filled_dict.get("four", 4), )
        # note that filled_dict.get("four") is still => None

        # set the value of a key with a syntax similar to lists
        filled_dict["four"] =   
        self.assertEqual(filled_dict["four"], )
        #
        # "setdefault()" inserts into a dictionary only if the given key isn't present
        filled_dict.setdefault("five", )  # filled_dict["five"] is set to 5
        self.assertEqual(filled_dict["five"], )
        filled_dict.setdefault("five", )  # filled_dict["five"] is still 5
        self.assertEqual(filled_dict["five"], )
        #
        # Sets store ... well sets (which are like lists but can contain no duplicates)
    def test_set(self):
        empty_set = set()
        # Initialize a "set()" with a bunch of values
        some_set = set([1, 2, 2, 3, 4])  # some_set is now set([1, 2, 3, 4])
        #
        # order is not guaranteed, even though it may sometimes look sorted
        another_set = set([4, 3, 2, 2, 1])  # another_set is now set([1, 2, 3, 4])
        #
        # Since Python 2.7, {} can be used to declare a set
        filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}
        
        # Add more items to a set
        self.assertEqual(5 in filled_set, )
        filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
        self.assertEqual(5 in filled_set, )
        self.assertEqual(filled_set, )

        # Do set intersection with &
        other_set = {3, 4, 5, 6}
        self.assertEqual(filled_set & other_set, )
        #
        # # Do set union with |
        self.assertEqual(filled_set | other_set, )
        #
        # Do set difference with -
        self.assertEqual({1, 2, 3, 4} - {2, 3, 5}, )
        #
        # Do set symmetric difference with ^
        self.assertEqual({1, 2, 3, 4} ^ {2, 3, 5}, )
        #
        # Check if set on the left is a superset of set on the right
        self.assertEqual({1, 2} >= {1, 2, 3}, )
        #
        # Check if set on the left is a subset of set on the right
        self.assertEqual({1, 2} <= {1, 2, 3}, )
        #
        # Check for existence in a set with in
        self.assertEqual(2 in filled_set, )
        self.assertEqual(10 in filled_set, )
        self.assertEqual(10 not in filled_set, )
        
    def test_type(self):
        # Check data type of variable
        li = []
        self.assertEqual(type(li), list)
        self.assertEqual(type({}), dict)
        self.assertEqual(type(5), int)
        self.assertEqual(type({1,2,3}), set)

if __name__ == '__main__':
    unittest.main()