# 1. Name:
#      Jaxon Hamm
#
# 2. Assignment Name:
#      Lab 13: Prime Numbers
#
# 3. Assignment Description:
#       This program will display all the prime numbers at or below a certain 
#       value. It will first prompt the user for an integer. If the integer is
#       less than 2, then the program will prompt the user for another number.
#       The program will then compute all the prime numbers below 
#       (and including) the given number. When finished, the program will 
#       display the list of prime numbers.
#
# 4. What was the hardest part? Be as specific as possible.
#       The assingment was pretty easy. I didn't run into any difficulties
#       implementing the algorithm. I also went sparse with asserts this time.
#       The reason for this is that I skipped areas that really have no reason
#       to mess up. Examples of things I skipped are the iterators in the loops
#       or places where the data had already been validated by other asserts.
#       I mainly focused on where data was being passed between functions,
#       stating my assumptions about what was coming into the function so it
#       would provide the expected output.
#
# 5. How long did it take for you to complete the assignment?
#      1 hour

#Get the number from the user
def get_num():
    valid = False
    number = 0
    while not valid:
        number = int(input(
            "This program will find all the prime numbers at or below N. Select that N: "))
        if number > 2:
            valid = True
        else:
            print("ERROR: Enter valid integer greater than 2")

    return number

# Find all the prime numbers up to and including the number passed.
def find_prime(number):
    assert(type(number) == type(1))
    assert(number > 2)
    is_prime = [True]*(number+1)
    
    # For the numbers between 2 and the root of the number, find all multiples.
    for factor in range(2, int(number**0.5)+1):
        if is_prime[factor]:
            for multiple in range(factor*2, number+1, factor):
                is_prime[multiple] = False
    
    # Turn the booleans into a list of primes.
    primes = [1]
    for index in range(2, number+1):
        if is_prime[index]:
            primes.append(index)

    return primes

# Run a test case.
def test_case(number):
    assert(type(number) == type(1))
    assert(number > 2)
    print("TEST CASE:", number)
    print("\tResultant primes: ", find_prime(number))

# Ask the user if thet would like to run the test cases
response = input("Are you running test cases? (y/n) ")
if response == 'y':
    test_case(10)
    test_case(53)
    test_case(100)
    test_case(200)
    print("TEST CASES: -1 through 2")
    get_num()

# Run the normal program as described in the header.
done = False
while not done:
    number = get_num()
    print("The prime numbers at or below 53 are", find_prime(number))

    # And then we do it again?
    response = ("Would you like to continue? (y/n) ")
    if response == 'n':
        done = True






