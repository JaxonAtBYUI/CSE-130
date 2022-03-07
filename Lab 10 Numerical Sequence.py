# 1. Name:
#      Jaxon Hamm
# 
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
#
# 3. Assignment Description:
#      This program will prompt the user for a positive integer n and then 
#      display the nth François number.
#
# 4. What was the hardest part? Be as specific as possible.
#      I couldn't set up an automated test case for the -1 and the 0 because  
#      they are considered invalid input and are caught in the function for 
#      getting a number from the user.
#
#      Once again, figuring out where I should be placing my asserts was a
#      a little challenging. I'm not entirely sure what is too much and what
#      makes sense to add an assert for.
#
# 5. How long did it take for you to complete the assignment?
#      45 minutes

#Get the number from the user
def get_num():
    valid = False
    number = 0
    while not valid:
        number = int(input("Which Francois number would you like to see? "))
        if number > 0:
            valid = True
        else:
            print("ERROR: Enter valid integer greater than 0")

    return number

# Define the francois function
def francois(n):
    # If the number is one of the set numbers.
    assert(n > 0)
    assert(type(n) == type(1))
    if n == 1:
        print("Francois number 1 is 2.")
        return
    elif n == 2:
        print("Francois number 2 is 1.")
        return

    # If the number is 3 or greater
    francois_num = 0
    values = [1, 2]
    for number in range(3, n+1):
        assert (number >= 3)
        assert (number < n+1)
        francois_num = values[0] + values[1]
        values[number % 2] = francois_num
    print("Francois number", n, "is", francois_num)
    return

# Run the program multiple times or do test cases.
response = input("Are you running test cases? (y/n) ")
if response == 'y':
    print('\nRUNNING TEST CASES')
    francois(1)
    francois(2)
    francois(9)
    francois(100)
    francois(200)
    print('\n')
    
    # Stop to keep the computer open.

done = False
while not done:
    n = get_num()
    assert(type(n) == type(1))
    francois(n)

    # Check if the user is done.
    response = input("Are you running test cases? (y/n) ")
    if response == 'y':
        done = True
