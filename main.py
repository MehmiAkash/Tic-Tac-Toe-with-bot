import os
import random
print(''' 
████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝''')


playagain=True
def show():
    print("\n___________________________________")
    print(f"       {gamearray[0]} | {gamearray[1]} | {gamearray[2]}")
    print(f"     -------------")
    print(f"       {gamearray[3]} | {gamearray[4]} | {gamearray[5]}")
    print(f"     -------------")
    print(f"       {gamearray[6]} | {gamearray[7]} | {gamearray[8]}")
    print("\n___________________________________")
    print(f"         {arr[0]}|{arr[1]}|{arr[2]} \n         {arr[3]}|{arr[4]}|{arr[5]} \n         {arr[6]}|{arr[7]}|{arr[8]}\n------------------------------------   ")
def check(sign):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if gamearray[a] == gamearray[b] == gamearray[c] == sign:
            return False
    return True
def defend(sign1,sign2,AI):
    defence_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    for combo in defence_combinations:
        a, b, c = combo
        values = [gamearray[a-1], gamearray[b-1], gamearray[c-1]]

        if values.count(sign1) == 2:
            if a in AI:
                return a
            if b in AI:
                return b
            if c in AI:
                return c
    return random.choice(AI)
def wincahance(sign1, sign2 , AI):
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    for combo in winning_combinations:
        a, b, c = combo
        values = [gamearray[a-1], gamearray[b-1], gamearray[c-1]]

        if values.count(sign2) == 2:
            if a in AI:
                return a
            if b in AI:
                return b
            if c in AI:
                return c
    return defend(sign1,sign2,AI)

while(playagain):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gamearray = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print("\n___________________________________")
    Player_select = input("Select the player X and O (Type X/O): ").upper()
    if (Player_select == 'X'):
        sign1 = 'X'
        sign2 = 'O'
    else:
        sign1 = 'O'
        sign2 = 'X'
    show()
    Mode = int(input("Select the mode by enter number for bot as second player is 1 and for dual is 0 :"))
    gameon = True
    if Mode == 1:
        gameonwithbot = True
    else:
        gameonwithbot = False
    AI = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chance = random.randint(0, 1)
    while (gameon):
        if chance == 0:
            i = int(input(f"{sign1}'s Turn- Type the number where you want to mark : "))
            os.system('cls||clear')
            while i not in AI or i < 1 or i > 9:
                print("Invalid input!. Please try again.")
                i = int(input(f"{sign1}'s Turn- Type the number where you want to mark: "))
            AI.remove(i)
            arr[i - 1] = '*'
            gamearray[i - 1] = sign1
            show()
            chance = 1
            if not check(sign1):
                gameonwithbot = False
                print(f'{sign1} Won the game 🎉🎉.')
                break
        if chance == 1:
            if gameonwithbot and gameon:
                j = wincahance(sign1, sign2, AI)
            elif gameon:
                j = int(input(f"{sign2}'s Turn- Type the number where you want to mark : "))
                while j not in AI or j < 1 or j > 9:
                    print("Invalid input!. Please try again.")
                    j = int(input(f"{sign1}'s Turn- Type the number where you want to mark: "))
            AI.remove(j)
            gamearray[j - 1] = sign2
            arr[j - 1] = '*'
            show()
            chance = 0
            if not check(sign2):
                gameon = False
                print(f'{sign2} Won the game 🎉🎉.')
                break
        if len(AI) == 0:
            gameon = False
            print("Game Draw 😁")
            break

    player=input("You want to play again ?(yes or no)").lower()
    if player=='no':
        playagain=False











