import random
import copy

temp = {}

def draw_validation(pl, ply, count):
    pl1 = copy.deepcopy(pl)
    keys = [i for i in pl1 if str(i).isdigit()]
    res1 = False
    # import pdb; pdb.set_trace()
    # for i in range(len(pl1)):
    #     if str(pl1[i]).isdigit():
    #         dd = pl1[i]
    #         pl1[i] = ply
    #         res1 = validation(pl1)
    #         if res1 == True:
    #             break
    #         else:
    #             pl1[i] = dd
    # return res1
    if ply == "X":
        if count == 7:
            pl1[keys[0]-1] = "X"
            pl1[keys[1]-1] = "O"
            res1 = validation(pl1)
            if res1 == True:
                res1 = "their is chance"
            else:
                pl1[keys[0]-1] = "O"
                pl1[keys[1]-1] = "X"
                res1 = validation(pl1)
            if res1 == True:
                res1 = "their is chance"
            else:
                res1 = "their is no chance"
        elif count == 8:
            pl1[keys[0]-1] = "X"
            res1 = validation(pl1)
            if res1 == True:
                res1 = "their is chance"
            else:
                res1 = "their is no chance"
    elif ply == "O":
        if count == 7:
            pl1[keys[0]-1] = "O"
            pl1[keys[1]-1] = "X"
            res1 = validation(pl1)
            if res1 == True:
                res1 = "their is chance"
            else:
                pl1[keys[0]-1] = "X"
                pl1[keys[1]-1] = "O"
                res1 = validation(pl1)
                if res1 == True:
                    res1 = "their is chance"
                else:
                    res1 = "their is no chance"
        elif count == 8:
            pl1[keys[0]-1] = "O"
            res1 = validation(pl1)
            if res1 == True:
                res1 = "their is chance"
            else:
                res1 = "their is no chance"

    return res1

def display(pl):
    print("\n")
    print("\t     |     |     ")
    print(f"\t  {pl[0]}  |  {pl[1]}  |  {pl[2]}  ")
    print("\t_____|_____|_____")
    print("\t     |     |     ")
    print(f"\t  {pl[3]}  |  {pl[4]}  |  {pl[5]}  ")
    print("\t_____|_____|_____")
    print("\t     |     |     ")
    print(f"\t  {pl[6]}  |  {pl[7]}  |  {pl[8]}  ")
    print("\t     |     |     ")
    print("\n")

def validation(pl):
    if pl[0] == pl[1] == pl[2]:
        return True
    elif pl[3] == pl[4] == pl[5]:
        return True
    elif pl[6] == pl[7] == pl[8]:
        return True
    elif pl[0] == pl[4] == pl[8]:
        return True
    elif pl[2] == pl[4] == pl[6]:
        return True
    elif pl[0] == pl[3] == pl[6]:
        return True
    elif pl[1] == pl[4] == pl[7]:
        return True
    elif pl[2] == pl[5] == pl[8]:
        return True
    else:
        return False

def game(pl):
    for i in range(9):
        if i%2 == 0:
            player1 = ""
            #to enter only integer
            while not player1.isdigit():
                print("please enter number in range(1-9) not string")
                player1 = input("player1 (%s) enter your position: "%temp['player1'])

            # to enter number in range of 1-9
            while int(player1) not in range(1,10):
                print("please enter number in range(1-9) not greater")
                player1 = input("player1 (%s) enter your position: "%temp['player1'])

            # to enter number in different position not occupied
            while not str(pl[int(player1)-1]).isdigit():
                print("position is already occupied, please enter proper position")
                player1 = input("player1 (%s) enter your position: "%temp['player1'])


            player1 = int(player1)
            pl[player1-1] = temp['player1']
            count = [i for i in pl if not str(i).isdigit()]
            display(pl)
            if len(count) == 7:
                res = validation(pl)
                if res != True:
                    res1 = draw_validation(pl, temp['player2'],len(count))
                    if res1 == 'their is no chance':
                        print("Draw match !!!!!!")
                        break
            elif len(count) == 8:
                res = validation(pl)
                if res != True:
                    res1 = draw_validation(pl, temp['player2'], len(count))
                    if res1 == 'their is no chance':
                        print("Draw match !!!!!!")
                        break
            res = validation(pl)
            if res == True:
                print("player1 won the game!!!")
                break
        else:
            player2 = ""
            #to enter only integer
            while not player2.isdigit():
                print("please enter number in range(1-9) not string")
                player2 = input("player2 (%s) enter your position: "%temp['player2'])

            # to enter number in range of 1-9
            while int(player2) not in range(1,10):
                print("please enter number in range(1-9) not greater")
                player2 = input("player2 (%s) enter your position: "%temp['player2'])

            # to enter number in different position not occupied
            while not str(pl[int(player2)-1]).isdigit():
                print("position is already occupied, please enter proper position")
                player2 = input("player2 (%s) enter your position: "%temp['player2'])

            player2 = int(player2)
            pl[player2-1] = temp['player2']
            count = [i for i in pl if not str(i).isdigit()]
            display(pl)
            if len(count) == 7:
                res = validation(pl)
                if res != True:
                    res1 = draw_validation(pl, temp['player1'])
                    if res1 == 'their is no chance':
                        print("Draw match !!!!!!")
                        break
            res = validation(pl)
            if res == True:
                print("player2 won the game!!!")
                break

def user_choice():

    val = ""
    while not (val.upper() == "X" or val.upper() == "O"):
        val = input("Do you want to be X or O :")
    val = val.upper()
    print(val)
    if val == "X" or val == "O":
        ll = ['player1', 'player2']
        player = random.choice(ll)
        pl = [1,2,3,4,5,6,7,8,9]
        print(f"you are {player}")
        display(pl)
        if val == "O" and player == "player1":
            temp[player] = val
            temp['player2'] = "X"
        elif val == "O" and player == "player2":
            temp[player] = val
            temp['player1'] = "X"
        elif val == "X" and player == "player1":
            temp[player] = val
            temp['player2'] = "O"
        elif val == "X" and player == "player2":
            temp[player] = val
            temp['player1'] = "O"
        print('player1 is %s'%temp['player1'])
        print('player2 is %s'%temp['player2'])
        game(pl)


choice = input("Do you want to start the game (Y or N):")
choice = choice.upper()
if choice == "Y":
    user_choice()
elif choice == "N":
    print("Thank you hvae a nice day!")
else:
    print("enter proper choice")
