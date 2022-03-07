# 1. Name:
#      Jaxon Hamm
#
# 2. Assignment Name:
#      Lab 08: Sort
#
# 3. Assignment Description:
#      This program will read a list of names from a file and sort them.
#
#  4. What was the hardest part? Be as specific as possible.
#      Honestly, I programmed it and it worked the first try. Other than adding
#      spaces to the end of some of the prompts there wasn't anything for me to
#      fix. 
#
#      Coming up with asserts was rather difficult. Some of them are definitely
#      redundant. I'm not entirely sure where I should be placing them. One
#      example is checking that filename is a string. It's guaranteed to be a
#      string because input always returns as a string. I can't quite see where
#      the asserts are necessary and where they are not. I feel like they would
#      go where you are unsure of somthing and this program is straightforward
#      enough that it doesn't seem to need asserts in too many places.
#  
# 5. How long did it take for you to complete the assignment?
#      It took me 40 minutes to complete.

import json

# Read json files to a list and return them for use.
def read_file(filename):
    # Read the file to a list
    with open(filename, "r") as file:
        assert type(filename) == type('string')
        text = file.read()
        data = json.loads(text)
        list = data['array']

    # Return the contents of the list in the file.
    assert type(list) == type([])
    return list

# Sort through the list linearly fashion and move the largest value to the end.
def linear_sort(list):
    
    # Go through list moving one forward from the back each time.
    for i_pivot in range((len(list)-1), 0, -1):
        i_largest = 0

        # Check every item before i_pivot.
        for i_check in range(0, i_pivot):
            assert i_check < i_pivot

            # If the value of i_check is bigger, set it as the largest value.
            if list[i_check] > list[i_largest]:
                i_largest = i_check
                assert len(list) > i_largest >= 0
        
        # If i_largest is bigger than i_pivot, switch their places.
        if list[i_largest] > list[i_pivot]:
            list[i_largest], list[i_pivot] = list[i_pivot], list[i_largest]
    
    return list

# Display the sorted list.
def display(list, filename):
    assert type(list) == type([])
    assert len(list) >= 0
    print("The values in", filename, "are:")
    for word in list:
        print("\t", word)

# Run the test case passed to the function.
def test_case(filename, case):
    print("TEST CASE: " + case)
    print("FILENAME: " + filename)

    # Read the list.
    assert type(filename) == type("string")
    list = read_file(filename)
    assert type(list) == type([])

    # Sort the list.
    list = linear_sort(list)
    assert type(list) == type([])

    # Print the list.
    display(list, filename)
    print("")
    return

# See if the user is running test cases.
response = input("Will you be running test cases? (y/n) ")
assert type(response) == type('y')
if response.lower() == 'y':
    test_case("Lab08.empty.json", "Empy list")
    test_case("Lab08.trivial.json", "List with one element")
    test_case("Lab08.languages.json", "Small list")
    test_case("Lab08.states.json", "Medium list")
    test_case("Lab08.cities.json", "Large list")

    # Stop the program so you can actually see the console
    input("")

# Run until they done. 
else:
    not_done = True
    while not_done:

        # Get the file and read it.
        filename = input("What is the name of the file? ")
        list = read_file(filename)
        assert type(list) == type([])

        # Sort the file.
        list = linear_sort(list)
        assert type(list) == type([])

        # Display the sorted list.
        display(list, filename)
        print("")

        # See if they are done yet.
        response = input("Are you done sorting? (y/n) ")
        assert type(response) == type('y')
        if response.lower() == 'y':
            not_done = False
