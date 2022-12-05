"""
RegEx: Regular Expression is a sequence of characters that forms a search pattern.
       RegEx can be used to check if a string contains the specified search pattern.
"""

import re

my_string = "This is a string"
m1 = re.search("^This.*string$", my_string)
print(m1)
