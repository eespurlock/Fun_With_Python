'''
Author: Esther Edith Spurlock

Title: Python Experiment Version 1
'''

def main():
    '''
    Gathers user's input and gives the appropriate output
    '''

    continue_code = "y" #this variable determines if we would like to continue
    while continue_code == "y":
        number = "not a number yet" #this variable holds the user's input
                                    #we initialize it as a non-numeric string so we can complete error handling
        while not number.isnumeric():
            number = input("Type in a number. ")
            if number.isnumeric():
                choose_function(number)
            else:
                print("This is not  number.")
        continue_code = input("Would you like to continue? y/n ")

def choose_function(number):
    '''
    Allows the user to choose which function to use on their inputted number
    
    Inputs:
        number: (string) a string of the user's number

    Outputs: the function the user wants to use
    '''
    choice = "not in dictionary" #this variable holds the user's choice
                                 #we initialize it to be a value that is not in the dictionary for error handling
    while choice not in function_dict:
        choice = input("What would you like to do with your number?\n" +
                       "1: Determine if it is even or odd\n" +
                       "2: Find what Fibonacci number is in that place\n" +
                       "3: Find the factorial of that number\n")
        if choice not in function_dict:
            print("This is not a valid choice.")
    function_dict[choice](number, int(number))

def is_even(number_string, number_int):
    '''
    Determines if the given number is even

    Inputs: 
        number_string: (string) a string of the number we will determine if it is even or odd    
        number_int: (int) the number we want to determine if it is even or odd
    
    Outputs: None, this will print to the command line whether the number is even or odd
    '''

    if number_int % 2 == 0:
            print(number_string + " is even.")
    else:
            print(number_string + " is odd.")

def fib_print(number_string, number_int):
    '''
    Prints what Fibonacci number comes in the place specified

    Inputs: 
        number_string: (string) a string of the number we want the Fibonacci number for    
        number_int: (int) the number we want to find the Fibonacci number for
    
    Outputs: None, this will print to the command line the Fibonacci number we want
    '''
    print("Place " + number_string + " in the Fibonacci sequence is " + str(fib_rec(number_int)))

def fib_rec(number, curr_place=1, fib_two=0, fib_one=0):
    '''
    Performs recursion to find the Fibonacci number in the nth place (n being the number the user originally inputted)

    Inputs:
        number: (int) the number that corresponds to a place in the Fibonnaci sequence
        curr_place: (int) the current place the regression is in in the Fibonacci sequence
        fib_two: (int) the Fibonacci number two places before the current place
        fib_one: (int) the Fibonacci number one place before the current place

    Outputs:
        curr_fib: (int) a Fibonacci number in the nth place in the sequence
    '''
    curr_fib = fib_two + fib_one #curr_fib stores the value of the current Fibonacci number
    
    #For the first place in our sequence, we have to specify that x = 1
    if curr_place == 1:
        curr_fib = 1

    #If our current place matches the place we want to go to, we will return the current Fibonacci number
    if number == curr_place:
        return(curr_fib)
    #If we need to keep going, we need to update our values before we call the recursion again
    else:
        curr_place += 1
        fib_two = fib_one
        fib_one = curr_fib
        return(fib_rec(number, curr_place, fib_two, fib_one))

def fact_print(number_string, number_int):
    '''
    Prints the factorial of the inputted number

    Inputs: 
        number_string: (string) a string of the number we want the factorial for    
        number_int: (int) the number we want to find the factorial for
    
    Outputs: None, this will print to the command line the factorial of the number
    '''
    print(number_string + "! is " + str(fact_rec(number_int)))

def fact_rec(number):
    '''
    Finds the factorial of a number using recursion

    Inputs: number: (int) the number we need to find the factorial for

    Outputs: (int) the factorial of our number
    '''
    #if we are at place 0, we return 1
    if number == 0:
        return(1)
    else:
        return(number * fact_rec(number - 1))

#store our different functions in a dictionary
function_dict = {"1": is_even, "2": fib_print, "3": fact_print}
main()

