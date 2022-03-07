# 1. Name:
#    Jaxon Hamm
#
# 2. Assignment Name:
#    Lab 02: Authentication
#
# 3. Assignment Description:
#    Use python to test various username password combinations found in a json
#    file and alert the user if they can use the system or not.
#
# 4. What was the hardest part? Be as specific as possible.
#    There was a really strange problem I ran into opening the file. Python
#    was throwing a lot of syntax errors asking for a colon. The only solution
#    I found was to delete all the code only to rewrite it all the same.
# 
#    I am also somewhat confused with importing fuuntions. From my what I
#    understand they are not in they python documentation so how do I know
#    what is built in? How do I know what the best practices are for those
#    functions? (i.e. We were told that it is not good practice to use break
#    and continue in our loops despite them being built into python. How is
#    that determined? How will I know what is not good convention if I'm
#    importing somthing I've never seen before?)
#    
# 5. How long did it take for you to complete the assignment?
# 20 minutes

# Import json so we can read .json files.
import json

# Define the funtion for authentication.
def auth_process():
    # Get the username and password combo to be tested.
    username = input("Username: ")
    password = input("Password: ")

    # Loop through the dictionary of credentials.
    authenticated = False

    for ind in range(len(credentials['username'])):
        if username == credentials['username'][ind]:
            if password == credentials['password'][ind]:
                authenticated = True

    # Notify the user if they have been authenticated
    if authenticated:
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")

# Read the JSON file into an object
with open("Lab02.json", "r") as file:
    text = file.read()
    credentials = json.loads(text)

file.close()

# Make a loop to make filming the whole process easier.
repeat = True

while repeat:
    auth_process()
    if input("Would you like to repeat? y/n ") == 'n':
        repeat = False 