# 1. Name:
#    Jaxon Hamm
#
# 2. Assignment Name:
#    Lab 03: Monopoly
#
# 3. Assignment Description:
#    Write a program to inform the user if he or she is able to build a hotel
#    on Pennsylvania Avenue. This program will ask the user several questions
#    and, based on these questions, tell the user whether a hotel can be
#    purchased for Pennsylvania and how much it will cost.
#
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was making the flow chart last week. I'm just not used
#    to making them. Because of that I just used the flowchart provided
#    
#    Aside from missing a return or two in the function there was no major
#    problem I ran into.
#
# 5. How long did it take for you to complete the assignment?
#     2 hours

#region FUNCTIONS
# Prompts the user for a valid Y/N input until the give it.
def prompt_YN(question):
    is_not_valid = True

    # Continue to prompt them until they put in a valid response.
    while is_not_valid:
        response = input(question)
        response = response.lower()
        if response == 'y' or response == 'n':
            return response
        else:
            print("Please input a valid y/n response.")

# Prompts the user for a valid integer input.
def prompt_int(question):
    is_not_valid = True

    # Continue to prompt them until they put in a valid response.
    while is_not_valid:
        response = input(question)
        
        if response.isdigit():
            return int(response)
        else:
            print("Please input a valid integer.")
    
# Prompts the user for a valid integer between 1 and 5.
def prompt_developement(question):
    is_not_valid = True
    while is_not_valid:
        response = prompt_int(question)
        if response <= 5 and response >= 0:
            return response
        else:
            print("Integer must be between 1 and 5.")
#endregion

# Determine if we are able to buy a hotel on the property or not.
def validate_hotel():

    # Determine if we own the necessary properties.
    own_properties = prompt_YN("Do you own all the green properties? (y/n) ")
    if own_properties == 'n':
        print(
            "You cannot purchase a hotel until you own"
            + " all the properties of a given color group.\n"
        )
        return

    # Determine what type of developement is on Pennsylvania
    developement_PA = prompt_developement("What is on Pennsylvania Avenue? "
    + " (0:nothing, 1:one house, ... 5:a hotel) ")
    if developement_PA == 5:
        print("You cannot purchase a hotel "
        +"if the property already has one.\n")
        return

    # Determine what type of developement is on North Carolina
    developement_NC = prompt_developement(
    "What is on North Carolina Avenue? "
    + " (0:nothing, 1:one house, ... 5:a hotel)")
    
    if developement_NC == 5:
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses.\n")
        return
    
    # Determine what type of developement is on Pacific Avenue
    developement_PC = prompt_developement(
        "What is on Pacific Avenue?"
        + " (0:nothing, 1:one house, ... 5:a hotel) ")

    if developement_PC == 5:
        print("Swap Pacific's hotel with Pennsylvania's 4 houses.\n")
        return

    # Determine how many hotels are available.
    is_not_valid = True
    hotels = 0
    while is_not_valid:
        hotels = prompt_int("How many hotels are there to purchase? ")
        if hotels >= 0:
            is_not_valid = False
        else:
            print("Integer must be between greater than or equal to 0")
    if hotels == 0:
        print("There are not enough hotels "
        + "available for purchase at this time.\n")
        return
    
    # See if the user has enough money to purchase the required property.
    properties_needed = (13 
        - developement_PA 
        - developement_NC 
        - developement_PC)
    cash_needed = properties_needed * 200
    available_cash = prompt_int("How much cash do you have to spend? ")
    if available_cash < cash_needed:
        print("You do not have sufficient funds "
        +"to purchase a hotel at this time.\n")
        return

    # Determine how many houses are left.
    houses_left = prompt_int("How many houses are there to purchase? ")
    if houses_left < (properties_needed - 1):       # -1 accounting for hotel.
        print("There are not enough houses "
        + "available for purchase at this time.\n")
        return

    # Output what the player must do to build a hotel on Pennsylvania.
    print("This will cost $", cash_needed, '.')
    print("\tPurchase 1 hotel and", (properties_needed - 1), "house(s).")
    print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
    if developement_NC < 4:
        print("\tPut", 4 - developement_NC, "house(s) on North Carolina.")
    if developement_PC < 4:
        print("\tPut", 4 - developement_PC, "house(s) on Pacific.")

    print('\n')
    return

# Simplest loop for running test cases.
while True:
    validate_hotel()