"""
Iterators: An iterator is an object that contains a countable number of values.
"""


my_tuple = ("a", "b", "d", 2)
my_it = iter(my_tuple)
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))

my_string = "My string"
my_it = iter(my_string)
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print()


class MyNumbers:
    def __iter__(self):
        self.index = 1
        return self

    def __next__(self):
        if self.index <= 100:
            x = self.index
            self.index += 1
            return x
        else:
            raise StopIteration


my_number = MyNumbers()
my_it = iter(my_number)
# print(next(my_it))
# print(next(my_it))
# print(next(my_it))
# print(next(my_it))

for i in my_it:
    print(i)
