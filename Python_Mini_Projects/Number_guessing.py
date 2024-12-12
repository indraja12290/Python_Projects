import random # Import the random module to generate random numbers


top_of_range = input("Type a number: ") # Enter user range of number


if top_of_range.isdigit():
    top_of_range = int(top_of_range) # Convert the input string to an integer

    if top_of_range <= 0: #need to enter a number greater than 0
        print("make sure enter a number larger than 0")
        quit()

else:
    print("please type a number")
    quit()

# Generate a random number between 0 and the user's input number (inclusive)
random_number = random.randint(0, top_of_range)
guesses = 0 # Initialize Guesses Variable

# Start a loop for the user to guess the random number
while True:
    guesses +=1 # Increment the number of guesses each time the loop runs
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please make sure enter a number")
        continue

    # Check if the user's guess matches the random number
    if user_guess == random_number:
        print("you won!")
        break
    
    # If the guess is too high, let the user know
    elif user_guess > random_number:
        print("you are above the number")
    else:
        print("Oops! you lost")


print("you got it in",  guesses , "guesses" )
      

