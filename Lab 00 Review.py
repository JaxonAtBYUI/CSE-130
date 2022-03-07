# Display Hello World on the screen.
print("Hello World")

# Display the class and number to the console.
print("This is CSE", 130)
print(f"This is CSE{130}")
print("This is CSE" + str(130))

class_number = 130
print("This is CSE", class_number)
print('This is "CSE', class_number, '"', sep='')

#Put the values two, four, and six on the screen where they are in a list.

#This is a set?
list_x = {2, 4, 6}
print(list_x)

#This is a list.
list_y = [2, 4, 6]
print(list_y)

#This is a tuple.
list_z = (2, 4, 6)
print(list_z)

#Display the values from 0 to 9.
for i in range(10):
    print(i)

# Loop until the user says "stop".
response = "go"
while not response == "stop":
    response = input("Are you done yet? ")