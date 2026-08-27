import random
import time

Text_intro_1 = """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number."""

Text_intro_2 = """Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)"""

class GameController:
    def __init__(self):
        self.level = 0
        self.number = 0
        self.score = 0
        self.first_number = 1
        self.high_score = 0
        self.last_number = 100

    def chances_game(self,level):
        self.level = level
        if self.level == 1:
            chances = 10
            name_level = "Easy"
        elif self.level == 2:
            chances = 5
            name_level = "Medium"
        elif self.level == 3:
            chances = 3
            name_level = "Hard"
        else:
            print("Pilih Nomor Yang Benar!")
            return None, None
        return chances, name_level

    def count_score(self, base_score, elapsed_time):
        final_score = round(base_score * elapsed_time, 2)
        if final_score > self.high_score:
            self.high_score = final_score
        return final_score

    
    
    def play_game(self, level):
        chances, name_level = self.chances_game(level)
        if chances is None:
            return
        
        print(f"Great! You have selected the {name_level} difficulty level.")
        print("Let's start the game!\n")

        next_game = "start"
        while next_game.lower() != "stop":
            secret_number = random.randint(self.first_number, self.last_number)
            guessed_correctly = False
            score = 0
            start_time = time.time()

            for attempt in range(1, chances + 1):
                input_number = int(input(f"Enter your guess ({self.first_number}-{self.last_number}): "))
                if input_number == secret_number:
                    print(f"Congratulations! You guessed the correct number in {attempt} attempts.\n")
                    guessed_correctly = True
                    score += 5
                    break 
                elif input_number > secret_number:
                    print(f"Incorrect! The number is less than {input_number}.\n")
                else:
                    print(f"Incorrect! The number is greater than {input_number}.\n")
            
            if not guessed_correctly:
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)
                final_score = self.count_score(score, elapsed_time)
                print(f"Game Over! The correct number is {secret_number}.")
                print(f"Time taken: {elapsed_time} seconds.")
                print(f"Your Session Score: {final_score}")
                print(f"Highest Score: {self.high_score}\n")
            next_game = input("Do you want to continue or not? (type 'stop' to quit): ")
            print()

def main():
    NumGues = GameController()
    print(Text_intro_1,"\n")
    print(Text_intro_2) 

    level_pilihan = int(input("Enter your choice: "))
    NumGues.play_game(level_pilihan)
    
if __name__ == "__main__":
    main()