class BrainGuesser:
    def _init_(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.current_guess = None

    def get_feedback(self):
        while True:
            feedback = input("Enter 'h' if the guess is too high, 'l' if too low, or 'c' if correct: ").lower()
            if feedback in ['h', 'l', 'c']:
                return feedback
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

    def guess(self):
        print("Think of a number between 1 and 100 (inclusive)...")

        play_again = 'y'
        while play_again == 'y':
            input("Press Enter when you're ready.")
            self.lower_bound = 1
            self.upper_bound = 100

            while True:
                self.current_guess = (self.lower_bound + self.upper_bound) // 2
                print(f"Is your number {self.current_guess}?")
                feedback = self.get_feedback()

                if feedback == 'h':
                    self.upper_bound = self.current_guess - 1
                elif feedback == 'l':
                    self.lower_bound = self.current_guess + 1
                else:
                    print(f"Yay! I guessed your number {self.current_guess}.")
                    break

            play_again = input("Do you want to play again? (y/n): ").lower()
            while play_again not in ['y', 'n']:
                print("Invalid input. Please enter 'y' or 'n'.")
                play_again = input("Do you want to play again? (y/n): ").lower()

if __name__ == "__main__":
    guesser = BrainGuesser()
    guesser.guess()
