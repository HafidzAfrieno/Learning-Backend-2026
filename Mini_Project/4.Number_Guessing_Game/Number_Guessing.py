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
        self.firt_number = 0
        self.last_number = 0

    def hange_game(self,level):
        self.level = level
        if self.level == 1:
            change = 10
            name_level = "Easy"
        elif self.level == 2:
            change = 5
            name_level = "Medium"
        elif self.level == 3:
            change = 3
            name_level = "Hard"
        else:
            print("Pilih Nomor Yang Benar!")
        return change,name_level

    def get_random_number(self):
        print()

    
def main():
    print(Text_intro_1,"\n")
    print(Text_intro_2) 

    NumGues = GameController()


if __name__ == "__main__":
    main()