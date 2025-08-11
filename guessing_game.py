import random  # Import the random module to generate a random number

# Friendly welcome message
print("🎯 Welcome to the Number Guessing Game!")
print("You have 7 chances to guess the correct number. Let's see if you can do it! 😎")

# Ask the player for the lower and upper range for the secret number
low = int(input("\n👉 Enter the Lower Bound: "))
high = int(input("👉 Enter the Upper Bound: "))

# Explain the rules again with the chosen range
print(f"\nAlright! I'm thinking of a number between {low} and {high}.")
print("You have exactly 7 attempts to guess it. Good luck! 🍀\n")

# Generate a random secret number in the given range
secret_number = random.randint(low, high)

# Game settings
total_chances = 7  # Total attempts allowed
guess_count = 0    # Counter to track number of guesses made

# Start the guessing loop
while guess_count < total_chances:
    guess_count += 1  # Increment the guess counter
    
    # Take user's guess
    try:
        guess = int(input(f"Attempt {guess_count}/{total_chances} - Your guess: "))
    except ValueError:
        print("⚠️ Oops! Please enter a valid number.")
        continue  # Skip this loop and ask again

    # Check if the guess is correct
    if guess == secret_number:
        print(f"✅ Woohoo! You guessed it right 🎉 The number was {secret_number}.")
        print(f"It took you {guess_count} attempt(s). 🏆")
        break  # Exit the loop since the game is won

    # If the guess is wrong and this was the last attempt
    elif guess_count == total_chances:
        print(f"❌ Out of chances! The number was {secret_number}. Better luck next time. 🙃")

    # Give hints based on whether the guess is too high or too low
    elif guess > secret_number:
        print("📉 Too high! Try guessing a smaller number.")
    elif guess < secret_number:
        print("📈 Too low! Try guessing a bigger number.")
