import random
import json
import os

# High score file
HIGH_SCORES_FILE = "high_scores.json"

def load_high_scores():
    """Load high scores from file or return default if file doesn't exist"""
    if os.path.exists(HIGH_SCORES_FILE):
        with open(HIGH_SCORES_FILE, 'r') as f:
            return json.load(f)
    return {"easy": 0, "medium": 0, "hard": 0}

def save_high_scores(scores):
    """Save high scores to file"""
    with open(HIGH_SCORES_FILE, 'w') as f:
        json.dump(scores, f)

def display_high_scores(scores):
    """Display the current high scores"""
    print("\n=== HIGH SCORES ===")
    print(f"Easy:   {scores['easy']}")
    print(f"Medium: {scores['medium']}")
    print(f"Hard:   {scores['hard']}")
    print("==================")

def calculate_score(max_attempts, attempts, max_hints, hint_count):
    """Calculate score using percentage-based system (70% attempts, 30% hints)"""
    attempt_ratio = (max_attempts - attempts + 1) / max_attempts
    hint_ratio = (max_hints - hint_count) / max_hints
    return min(100, int(attempt_ratio * 70 + hint_ratio * 30))

def get_hint(secret_number, last_guess, hint_count, max_hints):
    """Provide a helpful hint to the player"""
    if hint_count >= max_hints:
        print("\nNo more hints available!")
        return hint_count
    
    hint_count += 1
    difference = abs(secret_number - last_guess)
    
    if hint_count == 1:
        if secret_number % 2 == 0:
            print("\nHint: The number is even!")
        else:
            print("\nHint: The number is odd!")
    elif hint_count == 2:
        print(f"\nHint: The number is {'greater' if secret_number > last_guess else 'less'} than {last_guess}")
    elif hint_count == 3:
        if difference > 50:
            print("\nHint: You're very far from the number!")
        elif difference > 25:
            print("\nHint: You're quite far from the number!")
        elif difference > 10:
            print("\nHint: You're getting closer!")
        else:
            print("\nHint: You're very close!")
    
    remaining_hints = max_hints - hint_count
    print(f"Hints remaining: {remaining_hints}/{max_hints}")
    return hint_count

def number_guessing_game():
    """Main game function"""
    scores = load_high_scores()
    print("\nWelcome to the Number Guessing Game!")
    
    while True:
        # Difficulty selection
        print("\nChoose difficulty:")
        print("1. Easy (15 attempts, 3 hints)")
        print("2. Medium (10 attempts, 2 hints)")
        print("3. Hard (5 attempts, 1 hint)")
        
        try:
            difficulty = int(input("Enter choice (1-3): "))
            if difficulty not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Please enter a valid number (1-3)!")
            continue
        
        # Set game parameters based on difficulty
        if difficulty == 1:
            max_attempts = 15
            max_hints = 3
            difficulty_name = "easy"
        elif difficulty == 2:
            max_attempts = 10
            max_hints = 2
            difficulty_name = "medium"
        else:
            max_attempts = 5
            max_hints = 1
            difficulty_name = "hard"
        
        # Generate random number
        secret_number = random.randint(1, 100)
        attempts = 0
        hint_count = 0
        last_guess = None
        
        print(f"\nI'm thinking of a number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess it.")
        print(f"You can ask for {max_hints} hint(s) during the game (worth 30% of score).")
        print("Type 'hint' for help or 'quit' to exit.\n")
        
        while attempts < max_attempts:
            try:
                guess_input = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
                
                if guess_input.lower() == 'quit':
                    print(f"\nThe number was {secret_number}. Better luck next time!")
                    return
                elif guess_input.lower() == 'hint':
                    if last_guess is None:
                        print("\nMake at least one guess before asking for a hint!")
                        continue
                    hint_count = get_hint(secret_number, last_guess, hint_count, max_hints)
                    continue
                
                guess = int(guess_input)
            except ValueError:
                print("Please enter a valid number, 'hint', or 'quit'!")
                continue
            
            attempts += 1
            last_guess = guess
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                score = calculate_score(max_attempts, attempts, max_hints, hint_count)
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                print(f"Used {hint_count}/{max_hints} hints.")
                print(f"Your score: {score}/100")
                
                # Update high score if needed
                if score > scores[difficulty_name]:
                    print(f"New high score for {difficulty_name} difficulty!")
                    scores[difficulty_name] = score
                    save_high_scores(scores)
                
                display_high_scores(scores)
                break
        
        else:
            print(f"\nGame over! The number was {secret_number}.")
            display_high_scores(scores)
        
        # Play again?
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again == 'yes':
                break
            elif play_again == 'no':
                print("Thanks for playing! Goodbye.")
                return
            else:
                print("Please enter 'yes' or 'no'.")

# Start the game
if __name__ == "__main__":
    number_guessing_game()