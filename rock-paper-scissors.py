import random  # For computer's random choice

# 🎮 Game Introduction & Rules
print("""
🎯 Welcome to Rock, Paper, Scissors!

Winning Rules:
- Rock vs Paper    → Paper wins
- Rock vs Scissors → Rock wins
- Paper vs Scissors → Scissors wins
""")

# Main game loop — keeps running until the player decides to quit
while True:

    # Show available choices
    print("\nMake your move:")
    print("  1 - Rock 🪨")
    print("  2 - Paper 📄")
    print("  3 - Scissors ✂️")

    # Get player's choice and validate it
    try:
        choice = int(input("👉 Enter your choice (1/2/3): "))
    except ValueError:
        print("⚠️ Please enter a valid number (1, 2, or 3).")
        continue  # Restart loop

    # Keep asking until valid input is entered
    while choice not in [1, 2, 3]:
        choice = int(input("⚠️ Invalid choice. Please enter 1, 2, or 3: "))

    # Map choice number to name
    if choice == 1:
        player_choice = 'Rock'
    elif choice == 2:
        player_choice = 'Paper'
    else:
        player_choice = 'Scissors'

    # Show player's choice
    print(f"\n🧑 You chose: {player_choice}")

    # Computer makes its move randomly
    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        computer_choice = 'Rock'
    elif comp_choice == 2:
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissors'

    # Show computer's choice
    print(f"💻 Computer chose: {computer_choice}")
    print(f"\n🔍 {player_choice} vs {computer_choice}")

    # Determine winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'

    # Announce result
    if result == "DRAW":
        print("🤝 It's a tie!")
    elif result == player_choice:
        print("🎉 You win!")
    else:
        print("😢 Computer wins!")

    # Ask if player wants to play again
    play_again = input("\n🔄 Do you want to play again? (Y/N): ").lower()
    if play_again == 'n':
        break  # Exit the game loop

# Exit message
print("\n🙏 Thanks for playing Rock, Paper, Scissors! See you next time.")
