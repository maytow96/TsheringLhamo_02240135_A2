import random

class GameSystem:
    '''This is a game system that allows the user to play different games.
    The user can choose from the following games:
    1. Number guessing game
    2. Rock paper scissor game
    3. Trivia quiz game
    4. Pokemon card binder management
    '''
    def __init__(self):
        self.lives = 10
        self.score = 0
        self.binder = []  # For Pokemon Binder Manager
        self.num_guessing_score = 0
        self.rps_score = 0
        self.trivia_score = 0

    def num_guessing_game(self):
        '''Prompts the user to play a number guessing games.

    -each player is given 10 lives at the beginning.
    -As the game progress,each incorrect answer cost a live.
    -The game will be over if the player runs out of lives.
    - gets a point if the guess is correct.'''
        print("\nWelcome to the Number Guessing Game!")
        target = random.randint(1, 10)
        attempts = 0

        while self.lives > 0:
            try:
                user_choice = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            attempts += 1
            if user_choice == target:
                print("You guessed the number correctly!")
                print(f"Remaining lives: {self.lives}. Attempts: {attempts}. Current score: {self.score + 1}")
                self.num_guessing_score += 1
                self.score += 1
                break
            elif user_choice<target:
                self.lives -= 1
                print(f"guess higher . Lives remaining: {self.lives}. Try again.")

            elif user_choice>target:
                self.lives -= 1
                print(f"guess lower . Lives remaining: {self.lives}. Try again.")

        if self.lives == 0:
            print("You have run out of lives. Game over!")

    def rock_paper_scissor(self):
        """Prompt the players to play a rock-paper-scissors game.
        -with each win the player is awarded 5 points 
        -with each loss the player loses a life.
        -The game will be over if the player runs out of lives."""

        print("\nWelcome to Rock-Paper-Scissors!")
        if self.lives <= 0:
            print("You have no lives left. Game over!")
            return

        choices = ["rock", "paper", "scissors"]

        while True:
            computer_choice = random.choice(choices)
            user_choice = input("Choose rock, paper, or scissors: ").lower()

            if user_choice not in choices:
                print("Invalid choice. Please try again.")
                continue

            if computer_choice == user_choice:
                print(f"It's a tie! Both chose {user_choice}.")
                continue

            if (user_choice == "rock" and computer_choice == "scissors") or \
               (user_choice == "paper" and computer_choice == "rock") or \
               (user_choice == "scissors" and computer_choice == "paper"):
                print(f"You win! Computer chose {computer_choice}.")
                self.rps_score += 5
                self.score += 5
                break
            else:
                print(f"You lose! \n Computer chose {computer_choice}.")
                self.lives -= 1
                continue

        print(f"Current score: {self.score}. Lives remaining: {self.lives}.")

    def trivia_quiz_game(self):
        """Play a trivia quiz game."""
        if self.lives <= 0:
            print("You have no lives left. Game over!")
            return

        questions = {
            "Math": [
                {
                    "question": "What is the value of pi?",
                    "options": ["A. 2.14", "B. 3.14", "C. 3.146", "D. 3"],
                    "answer": "B"
                },
                {
                    "question": "Which of the following is not a valid python python data",
                    "options":["A.int","B.string","C.float","D.boolean"],
                    "answer": "B"
                }
            ],
            "Movies": [
                {
                    "question": "Which god is associated with thunder and lightning?",
                    "options": ["A. Odin", "B. Thor", "C. Loki", "D. Valkyrie"],
                    "answer": "B"
                },
                {
                    "question": "Who is the first Avenger?",
                    "options": ["A. Iron Man", "B. Hulk", "C. Captain America", "D. Black Widow"],
                    "answer": "C"
                }
            ]
        }

        completed_categories = set()

        while len(completed_categories) < len(questions):
            remaining_categories = [cat for cat in questions if cat not in completed_categories]
            category = random.choice(remaining_categories)
            question = random.choice(questions[category])

            print(f"\nCategory: {category}")
            print(question["question"])
            for option in question["options"]:
                print(option)

            answer = input("Your answer (A, B, C, D): ").strip().upper()
            if answer == question["answer"]:
                print("Correct!")
                self.score += 10
                completed_categories.add(category)
            else:
                print(f"Wrong! The correct answer was {question['answer']}.")
                self.lives -= 1

            if self.lives <= 0:
                print("You have run out of lives. Game over!")
                return

        print("Congratulations! You completed the quiz.")
        print(f"Final score: {self.score}.")

    def pokemon_binder_game(self):
        '''Manage a Pokemon card binder.
        -user can add cards to the binder.
        -user can reset the binder.
        -user can view the current binder contents.'''
        print("\nWelcome to the Pokemon Binder Manager!")
        while True:
            print("\n1. Add card")
            print("2. Reset binder")
            print("3. View current binder")
            print("4. Return to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    card = int(input("Enter the Pokemon card number from 1-1025: "))
                    if card < 1 or card > 1025:
                        print("Invalid card number. Please enter a number from 1-1025")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                self.binder.append(card)
                print(f"{card} added to the binder.")
            elif choice == "2":
                self.binder.clear()
                print("Binder reset.")
            elif choice == "3":
                print("Current binder contents:")
                if self.binder:
                    for card in self.binder:
                        print(f"- {card}")
                else:
                    print("Binder is empty.")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def view_score(self):
        '''View the current score and lives.
        -user can view the current score and lives.
        -if the player runs out of lives the game will be over hence have to run the program again'''        
        print(f"Total score: {self.score}. Lives remaining: {self.lives}.")

    def main_menu(self):
        """Main menu for the game system."""
        while True:
            print("\nSelect a game or option:")
            print("0. Exit")
            print("1. Number Guessing Game")
            print("2. Rock-Paper-Scissors")
            print("3. Trivia Quiz")
            print("4. Pokemon Binder Manager")
            print("5. View Total Score")

            choice = input("Enter your choice: ")

            if choice == "0":
                print("Game over. Thanks for playing!")
                break
            elif choice == "1":
                self.num_guessing_game()
            elif choice == "2":
                self.rock_paper_scissor()
            elif choice == "3":
                self.trivia_quiz_game()
            elif choice == "4":
                self.pokemon_binder_game()
            elif choice == "5":
                self.view_score()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game_system = GameSystem()
    game_system.main_menu()