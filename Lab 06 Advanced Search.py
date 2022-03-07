# 1. Name:
#      Jaxon Hamm
#
# 2. Assignment Name:
#      Lab 06: Advanced Search
#
#  3. Assignment Description:
#       Read the contents of the file into a list. The program will then prompt
#       the user for a name. Finally, we will tell the user whether the name is 
#       in the list.
#
# 4. Algorithmic Efficiency
#      The efficiency is O(log(n)). This is because the rule is as long as the
#      start is less than the end, continue running. The rule for how the start 
#      and end move is the list is cut in half each iteration until the start
#      and end swithc places with each other. Because of this, if the list is
#      doubled in size, the list would require one extra iteration. Thus, the
#      algorithmic efficiency is O(log2(n))
# 
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part of writing this program was that I did not understand.
#      how the .json files were formatted so the list.len() was returning as 1.
#      I ended up just had to reference index 0 each time I called list and
#      that fixed the prblem. It took me a while to find that. 
#
# 6. How long did it take for you to complete the assignment?
#      1 hour and 15 minutes

import json
#region FUNCTIONS
def read_file(filename):
    # Read the file to a list
    with open(filename, "r") as file:
        text = file.read()
        list = json.loads(text)

    # Return the contents of the list in the file.
    return list

def binary_search(word, list):
    # Define the start and end of the list.
    start = 0
    end = len(list['array']) - 1

    # Search list by cutting it in half each iteration.
    while start <= end:
        pointer = int((start + end) / 2)
        pointer_value = list['array'][pointer]

        # If we went past the word.
        if pointer_value > word:
            end = pointer - 1

        # If the word is further in the list.
        elif pointer_value < word:
            start = pointer + 1

        # If the value is found, return true.
        elif pointer_value == word:
            return True

    # If the value is not found return false.
    return False

# Display the results of the search to the user.
def display_result(word, list, filename):
    if binary_search(word, list):
        print("We found " + word + " in " + filename + ".")
    else:
        print("We did not find " + word + " in " + filename + ".")

# Run through the test case information given to the function.
def test_cases(test_case, filename, word):

    # Print the test case, read the file, and get the output.
    print("TEST CASE: " + test_case)
    print("Filename:" + filename)
    print("Name: " + word)
    list = read_file(filename)

    display_result(word, list, filename)
    print("\n")
#endregion

# Ask the user if we are running test cases.
response = input("Are you running test cases? (y/n) ")

# If we are running test, run the test cases.
if response == 'y':
    test_cases("Empty List", "Lab06.empty.json", "Empty")
    test_cases("Single item found", "Lab06.trivial.json", "trivial")
    test_cases("Single item not found", "Lab06.trivial.json", "missing")
    test_cases("Small list found", "Lab06.languages.json", "C++")
    test_cases("Small list not found", "Lab06.languages.json", "Lisp")
    test_cases("Big list found", "Lab06.countries.json", 
    "United States of America")
    test_cases("Big list not found", "Lab06.countries.json", "United States")

    test = input("PRESS ENTER TO EXIT")

# If the user is using the program normally, enter normal usage.
else:
    continue_usage = 'y'
    while continue_usage == 'y':

        # Get the filename from the user and save the data to a list.
        filename = input("What is the name of the file? ")
        list = read_file(filename)

        # Get the word and then search the list for the word.
        word = input("What name are we looking for? ")
        if binary_search(word, list):
            print("We found " + word + " in " + filename + ".")
        else:
            print("We did not find " + word + " in " + filename + ".")

        # Ask the user if they would like to continue searching files.
        continue_usage = input("Would you like to test another file? (y/n) ")
        print("\n")


