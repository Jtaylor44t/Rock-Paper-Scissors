#things to improve... add a player name function, score keeper, also allow enter of lower case. like rock,paper,scissors


from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]


#assign a random play to the computer
computer = t[randint(0,2)]

playername = input("Enter player name: ")



#set player to False
player = False


while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?").lower()
    if player == computer:
        print("Tie!")
    elif player == "Rock".lower():
        if computer == "Paper":
            print(f"You lose {playername}!", computer.title(), "covers", player)
        else:
            print(f"You win {playername}!", player.title(), "smashes", computer)
    elif player == "Paper".lower():
        if computer == "Scissors":
            print(f"You lose {playername}!", computer.title(), "cut", player) 
        else:
            print(f"You win {playername}!", player.title(), "covers", computer) 
    elif player == "Scissors".lower():
        if computer == "Rock":
            print(f"You lose {playername}...", computer.title(), "smashes", player) 
        else:
            print(f"You win {playername}!", player.title(), "cut", computer)
    else:
        print(f"That's not a valid play {playername}. Check your spelling!") 
#player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
