"""
Sets: Set is a collection that is unordered, unmodifiable and unindexed.
      No duplicate members
"""

vowels = {"a", "e", "i", "o", "u", "y"}
print(vowels)

# Get the length
print(len(vowels))
print()

# Access Items: You cannot access items in a set by referring to an index or a key
set1 = {12, "23", 2, 5}
for i in set1:
    print(i)
print()

# Add items
vowels = {"a", "e", "i", "o", "u"}
vowels.add("y")
print(vowels)
print()

# Add sets or lists or tuple or sets
vowel1 = {"a", "e", "i"}
vowel2 = {"o", "u", "y"}
vowel1.update(vowel2)
print(vowel1)

vowels.add("y")
print()
