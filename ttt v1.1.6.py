Tic Tac Toe - v1.1.5

#optimized pvp playing system
#dumb AI installed

from smart_ai_v3 import *
import random

class game:
    def pvp(self):
        
        print("");print("");print("BOARD:");print("")

        board = []
        for i in range(3):
            board.append(["."]*3)

        for i in board:
            print(" ".join(i))
            print("")

        show1 = [1,2,3]#instruction board
        show2 = [4,5,6]
        show3 = [7,8,9]

        win = False
        while not win:

            print("")
            print("Enter for the spaces:")
            print("")

            print(show1)
            print(show2)
            print(show3)

            turn = 0

            while turn < 2:
                enter = False
                while not enter:#gets user space
                    if turn == 0:
                        print("Player 1's Turn (X)")
                    else:
                        print("Player 2's Turn (O)")
                    try:
                        pos = int(input("Enter Move: "))
                        if 0 < pos < 10:
                            if 1 <= pos <= 3:
                                pos1 = 0
                                pos2 = pos - 1
                            elif 4 <= pos <= 6:
                                pos1 = 1
                                pos2 = pos - 4
                            else:
                                pos1 = 2
                                pos2 = pos - 7
                            if not board[pos1][pos2] == ".":
                                print("That space is taken.")
                                enter = False
                            else:
                                enter = True
                        else:
                            print("That is not a valid space.")
                            enter = False
                    except:
                        print("Error.")
                        
                if turn == 0:
                    if board[pos1][pos2] == ".":
                        board[pos1][pos2] = "X"#executes the move
                        print("YES")
                        enter = True
                elif turn == 1:
                    if board[pos1][pos2] == ".":
                        board[pos1][pos2] = "O"
                        enter = True

                for i in board:
                    print(" ".join(i))#updates board

                for i in board:
                    if all(x == i[0] for x in i) == True:
                        if i[0] == "X":
                            player = 1
                            win = True
                            turn = 2
                        elif i[0] == "O":
                            player = 2
                            win = True
                            turn = 2

                c1 = [board[0][0],board[1][0],board[2][0]]
                c2 = [board[0][1],board[1][1],board[2][1]]
                c3 = [board[0][2],board[1][2],board[2][2]]
                d1 = [board[0][0],board[1][1],board[2][2]]
                d2 = [board[0][2],board[1][1],board[2][0]]
                all_check = [c1,c2,c3,d1,d2]

                for i in all_check:
                    if all(x == i[0] for x in i) == True:
                        if i[0] == "X":
                            player = 1
                            turn = 2
                            win = True
                        elif i[0] == "O":
                            player = 2
                            turn = 2
                            win = True

                draw = True
                for i in board:
                    for e in i:
                        if e == ".":
                            draw = False
                if draw == True:
                    player = 3
                    win = True

                turn += 1

        if player == 1:
            print("Player 1 Won!")
        elif player == 2:
            print("Player 2 Won!")
        else:
            print("Draw...")

    def dumbAI(self):

        print("");print("");print("BOARD:");print("")

        board = []
        for i in range(3):
            board.append(["."]*3)

        available_pos = [0,1,2,3,4,5,6,7,8]
        spaces = [] 
        for i in board:
            for e in i:
                spaces.append(e)

        for i in board:
            print(" ".join(i))
            print("")

        show1 = [1,2,3]#instruction board
        show2 = [4,5,6]
        show3 = [7,8,9]

        if self.who_starts():
            player = True
            print("Player Starts.")
        else:
            player = False
            print("AI Starts.")

        change = False

        win = False
        while not win:

            if change:
                player = not player

            print("")
            print("Enter for the spaces:")
            print("")

            print(show1)
            print(show2)
            print(show3)

            if player:

                enter = False
                while not enter:#gets user space
                    print("Player's Turn (X)")
                    try:
                        pos = int(input("Enter Move: "))
                        if 0 < pos < 10:
                            if 1 <= pos <= 3:
                                pos1 = 0
                                pos2 = pos - 1
                            elif 4 <= pos <= 6:
                                pos1 = 1
                                pos2 = pos - 4
                            else:
                                pos1 = 2
                                pos2 = pos - 7
                            if not board[pos1][pos2] == ".":
                                print("That space is taken.")
                                enter = False
                            else:
                                enter = True
                        else:
                            print("That is not a valid space.")
                            enter = False
                    except:
                        print("Error.")

                if board[pos1][pos2] == ".":
                    board[pos1][pos2] = "X"#executes the move
                    enter = True

            elif not player:

                use_pos = []

                for i in spaces:
                    if not i == ".":#if landed on
                        print(spaces,spaces.index(i),i,available_pos)
                        del available_pos[spaces.index(i)]
                        del spaces[spaces.index(i)]

                for i in available_pos:
                    use_pos.append(i)

                random.shuffle(use_pos)

                pos = use_pos[random.randint(0,len(use_pos)-1)]

                if 0 <= pos <= 2:
                    pos1 = 0
                    pos2 = pos
                elif 3 <= pos <= 5:
                    pos1 = 1
                    pos2 = pos - 3
                else:
                    pos1 = 2
                    pos2 = pos - 6

                while not board[pos1][pos2] == ".":

                    pos = use_pos[random.randint(0,len(use_pos)-1)]

                    if 0 <= pos <= 2:
                        pos1 = 0
                        pos2 = pos
                    elif 3 <= pos <= 5:
                        pos1 = 1
                        pos2 = pos - 3
                    else:
                        pos1 = 2
                        pos2 = pos - 6

                board[pos1][pos2] = "O"

            change = True

            for i in board:
                print(" ".join(i))#updates board

            for i in board:
                if all(x == i[0] for x in i):
                    if i[0] == "O":
                        player = 2
                        win = True
                    elif i[0] == "X":
                        player = 1
                        win = True

            c1 = [board[0][0],board[1][0],board[2][0]]
            c2 = [board[0][1],board[1][1],board[2][1]]
            c3 = [board[0][2],board[1][2],board[2][2]]
            d1 = [board[0][0],board[1][1],board[2][2]]
            d2 = [board[0][2],board[1][1],board[2][0]]
            all_check = [c1,c2,c3,d1,d2]

            for i in all_check:
                if all(x == i[0] for x in i):
                    if i[0] == "O":
                        player = 2
                        win = True
                    elif i[0] == "X":
                        player = 1
                        win = True

            draw = True
            for i in board:
                for e in i:
                    if e == ".":
                        draw = False
            if draw == True:
                player = 3
                win = True

        if player == 1:
            print("Player Won!")
        elif player == 2:
            print("AI Won!")
        else:
            print("Draw...")

    def smartAI(self):

        print("");print("");print("BOARD:");print("")

        board = []
        for i in range(3):
            board.append(["."]*3)

        for i in board:
            print(" ".join(i))
            print("")

        show1 = [1,2,3]#instruction board
        show2 = [4,5,6]
        show3 = [7,8,9]

        if self.who_starts():
            ai_starts = True
        else:
            ai_starts = False

        win = False

        if ai_starts:
            while not win:
                


    def who_starts(self):

        who = random.randint(1,100)
        if who <= 50:
            return True
        else:
            return False

    def execute(self,which):
        if which == "pvp":
            self.pvp()
        elif which == "dumb":
            self.dumbAI()
        elif which == "smart":
            self.smartAI()


run = game()

done = False
while not done:
    go = input("Play? - Y/N: ")
    if go == "Y" or go == "y":
        which = input("1 or 2 players: ")
        print("")
        if which == "1":
            level = input("Choose your difficulty: Easy/Hard: ")
            if level == "E" or level == "e":
                run.execute("dumb")
            elif level == "H" or level == "h":
                run.execute("smart")
            else:
                print("Error.")
        elif which == "2":
            run.execute("pvp")
        else:
            print("Error.")
    elif go == "N" or go == "n":
        done = True
    else:
        print("Error.")
        print("")
print("Goodbye.")
