# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [item for item in range(1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [item ** 3 for item in range(0, 10)] # item **3 gets evaluated everytime the loop runs

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [letter.upper() for letter in a]
 
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [int(item) for item in x if int(item) % 2 == 0]
#split was causing it to be returned as a string but we need to coerse it to an int
print(y)

