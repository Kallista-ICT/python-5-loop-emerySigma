import random

# initialize Variables
score = 0
rolls = []

# display a Welcome Message
print("Welcome to the Dice Game")
print("Your goal is to reach a score of 50 or more by rolling a die.")
print("Lets start\n")


# keep the game running as long as the score is < 50.
while score < 50:
    
    # ask the Player to roll the Die
    input("Press Enter to roll the die...")
    die = random.randint(1, 6)

    # add the value of the roll to the score and record the roll in the list.
    score += die
    rolls.append(die)

    # Display the roll Result and Current Score
    print(f"\nYou rolled a {die}.")
    print(f"Your current score is {score}.\n")


# once the score is 50 or more, display congratulation message.
print("Congratulations! You reached 50 points or more!")
print(f"Your final score is: {score}")
print(f"Your rolls during the game: {rolls}")
