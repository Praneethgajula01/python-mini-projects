# typing_speed_test.py
# A simple, friendly Typing Speed Test.
# Shows a random sentence, times your typing, and prints WPM & accuracy.

import time
import random
import textwrap

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Learning to code is a superpower — use it wisely.",
    "Python makes simple things easy and hard things possible.",
    "Small steps every day lead to big changes over time.",
    "Creativity is intelligence having fun.",
    "Typing fast is great, but accuracy wins the race.",
    "Coffee, code, repeat.",
    "Never stop asking questions and solving problems."
]

def pick_sentence():
    """Return a random sentence from the list."""
    return random.choice(SENTENCES)

def calculate_accuracy_and_errors(reference: str, typed: str):
    """
    Compare reference and typed strings character-by-character.
    Returns (accuracy_percent, correct_chars, total_chars, errors, extra_chars).
    - correct_chars: number of chars that match at same position
    - total_chars: length of the reference sentence
    - errors: positions where typed char != reference char (up to len(reference))
    - extra_chars: additional characters typed beyond the reference (penalized)
    """
    correct = 0
    errors = 0
    for i, ref_ch in enumerate(reference):
        if i < len(typed) and typed[i] == ref_ch:
            correct += 1
        else:
            errors += 1

    # Extra characters typed beyond the reference length
    extra_chars = max(0, len(typed) - len(reference))

    total_chars = len(reference)
    accuracy = (correct / total_chars) * 100 if total_chars else 0.0

    return round(accuracy, 2), correct, total_chars, errors, extra_chars

def calculate_wpm(typed_text: str, elapsed_seconds: float):
    """
    Compute Words Per Minute (WPM).
    Common formula: WPM = (number_of_characters / 5) / minutes
    """
    if elapsed_seconds <= 0:
        return 0.0
    num_chars = len(typed_text)
    minutes = elapsed_seconds / 60
    wpm = (num_chars / 5) / minutes
    return round(wpm, 2)

def display_centered_multiline(text, width=70):
    """Prints wrapped text nicely centered-ish for readability."""
    for line in textwrap.wrap(text, width=width):
        print(line)

def main():
    print("\n⌨️  Typing Speed Test — Ready, steady, type!\n")
    try:
        while True:
            sentence = pick_sentence()
            print("Type the following sentence exactly and press Enter when done:\n")
            display_centered_multiline(f"\"{sentence}\"\n")

            input("Press Enter when you're ready to start...")

            # Start timer
            start_time = time.time()
            typed = input("\nYour attempt: ")
            end_time = time.time()

            elapsed = end_time - start_time
            wpm = calculate_wpm(typed, elapsed)
            accuracy, correct_chars, total_chars, errors, extra = calculate_accuracy_and_errors(sentence, typed)

            # Show results
            print("\n⏱ Results")
            print(f" Time taken       : {round(elapsed, 2)} seconds")
            print(f" Words per minute : {wpm} WPM")
            print(f" Accuracy         : {accuracy}% ({correct_chars}/{total_chars} correct chars)")
            if errors > 0:
                print(f" Mistakes         : {errors} mismatched characters within sentence")
            if extra > 0:
                print(f" Extra chars      : {extra} character(s) typed beyond the sentence (penalized in accuracy)")

            # Helpful feedback
            if accuracy == 100:
                print(" 🌟 Perfect! Flawless typing.")
            elif accuracy >= 90:
                print(" 👍 Great job — just a few slips.")
            elif accuracy >= 70:
                print(" 🙂 Not bad — keep practicing to improve speed and accuracy.")
            else:
                print(" 💪 Practice more — focus on accuracy first, then speed.")

            # Play again?
            again = input("\nDo you want to try again? (Y/N): ").strip().lower()
            if again == 'n':
                break

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nInterrupted. Goodbye — keep practicing! 👋")

    print("\nThanks for playing the Typing Speed Test. Happy coding! 🐍\n")

if __name__ == "__main__":
    main()
