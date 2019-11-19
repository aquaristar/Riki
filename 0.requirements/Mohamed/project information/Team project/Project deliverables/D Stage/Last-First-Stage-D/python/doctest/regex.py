"""
This is the regex example module
Ues this site for your regex practice
    https://www.tutorialspoint.com/python/python_reg_expressions.htm
"""
import re

def regex1(str):
    """checks if input str has the form 'ab*'

    >>> regex1("abbbbbb")
    'abbbbbb'
    >>> regex1("bbbbbbb")
    """
    p = re.compile()
    m = p.match(str)
    if m:
        return m.group(0)
    else:
        return None

def regex2(str):
    """checks if input str has the form 'a(b*)'

    >>> regex2("abbbbbb")
    'bbbbbb'
    >>> regex2("bbbbbbb")
    """
    p = re.compile()
    m = p.match(str)
    if m:
        return m.group(1)
    else:
        return None

def regex3(str):
    """checks if input str has the form '^[a-z][A-Z]+$'

    >>> regex3("Life is short")
    ['Life', 'is', 'short']
    >>> regex3("123456")
    []
    """
    p = re.compile()
    return p.findall(str)

def regex4(str):
    """checks if input has Python followed by ! => '(Python)(?=!)!'

    >>> regex4("Python!??")
    'Python'
    >>> regex4("Python")
    """
    p = re.compile()
    m = p.match(str)
    if m:
        return m.group(1) 
    else:
        return None

def regex5(str):
    """checks if input has Python is *not* followed by ! => '(Python)(?!!)'

    >>> regex5("Python!??Bad")
    >>> regex5("PythonGood")
    'Python'
    """
    p = re.compile()
    m = p.match(str)
    if m:
        return m.group(1) 
    else:
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()