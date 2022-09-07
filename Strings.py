# So what is a string a string is just a sequence of characters.
# Those characters can be any combination of numbers spaces uppercase letters lowercase letters underscores
# or symbols such as a period or exclamation point.
# strings also count as spaces
string = "This is a string"
print(string[4])

# String Slicing
Example = "oranges"

print(Example[:2])  # 2nd letter and before

print(Example[3:7])  # From letter 3 to letter 7

print(Example[0:])  # From letter 0 and `on`wards

# Concatination
print("string" + " " + "example")

# Example

New = "Capalot Polo G"
sliced = New[8:]
print(New)
print(sliced)

# String Exercise
ex_9 = "Just do it!"
print(ex_9[10])

print(ex_9[5:7])

print(ex_9[8:11])

print(ex_9[0:4])

print("don't" + " " + ex_9[5:])
