import random
import time

class is_valid_move:
    def __init__(self, position, metrix):
        self.position = position
        self.metrix = metrix

    def check(self):

        match self.position:
            case "1":
                return self.metrix[0][0] == ""
            case "2":
                return self.metrix[0][1] == ""
            case "3":
                return self.metrix[0][2] == ""
            case "4":
                return self.metrix[1][0] == ""
            case "5":
                return self.metrix[1][1] == ""
            case "6":
                return self.metrix[1][2] == ""
            case "7":
                return self.metrix[2][0] == ""
            case "8":
                return self.metrix[2][1] == ""
            case "9":
                return self.metrix[2][2] == ""
            case _:
                return False

class insert_user_choice:
    def __init__(self, position, metrix, symbol):
        self.position = position
        self.metrix = metrix
        self.symbol = symbol

    def insert(self):
        match self.position:
            case "1":
                self.metrix[0][0] = self.symbol
            case "2":
                self.metrix[0][1] = self.symbol
            case "3":
                self.metrix[0][2] = self.symbol
            case "4":
                self.metrix[1][0] = self.symbol
            case "5":
                self.metrix[1][1] = self.symbol
            case "6":
                self.metrix[1][2] = self.symbol
            case "7":
                self.metrix[2][0] = self.symbol
            case "8":
                self.metrix[2][1] = self.symbol
            case "9":
                self.metrix[2][2] = self.symbol
            case _:
                return False


class Game:

    def __init__(self, name):
        self.name = name
        self.metrix = [
                        ["", "", ""],
                        ["", "", ""],
                        ["", "", ""]
                    ]

    def display_board(self):
        for i, row in enumerate(self.metrix):
            row_display = " | ".join(f"{cell:2}" for cell in row)
            print(" " + row_display)
            if i < len(self.metrix) - 1:
                print(" ---+---+---")


    def check_win(self):

        for col in range(len(self.metrix)):
            if self.metrix[0][col] == self.metrix[1][col] == self.metrix[2][col] and self.metrix[0][col] != "":
                return True

        for row in range(len(self.metrix)):
            if self.metrix[row][0] == self.metrix[row][1] == self.metrix[row][2] and self.metrix[row][0] != "":
                return True

        if self.metrix[0][0] == self.metrix[1][1] == self.metrix[2][2] and self.metrix[0][0] != "":
            return True
        if self.metrix[0][2] == self.metrix[1][1] == self.metrix[2][0] and self.metrix[2][0] != "":
            return True

        return False
    def check_draw(self):
        for row in self.metrix:
            if "" in row:
                return False
        return True


    def play(self):
        print("Welcome " + self.name)
        print("Let's play!")
        self.display_board()
        while True:
            while True:
                user_choice = input("Enter number: 1-9 ")
                valid_move = is_valid_move(user_choice, self.metrix)
                if valid_move.check():
                    inserter = insert_user_choice(user_choice, self.metrix, 'X')
                    inserter.insert()
                    self.display_board()
                    if self.check_win():
                        print("You win!")
                        return

                    if self.check_draw():
                        print("It's a draw")
                        return
                    break
                else:
                    print("Invalid choice, try again..")
            while True:
                time.sleep(1)
                computer_choice = str(random.randint(1, 9))
                valid_move = is_valid_move(computer_choice, self.metrix)
                if valid_move.check():
                    inserter = insert_user_choice(computer_choice, self.metrix, "O")
                    inserter.insert()
                    self.display_board()
                    if self.check_win():
                        print('You lose!')
                        print("Computer wins!")
                        return

                    if self.check_draw():
                        print("It's a draw")
                        return
                    break


if __name__ == '__main__':
    name = input("Please enter your name: ")
    game = Game(name)
    game.play()
