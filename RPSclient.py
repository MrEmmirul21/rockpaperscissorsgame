import socket
import threading

host = '192.168.56.103'
port = 8888
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
choices = ['R', 'P', 'S', "s", "p", "r"]
try:
    client.connect((host, port))
except socket.error as e:
    print(str(e))

print(" Waiting for other player")

def send_data(data):
    client.send(data.encode("utf-8"))

def game():
    i = 0
    score1 = 0
    score2 = 0
    while i<5:
        choice = input(" Rock/Paper/Scissors : ")
        if choice in choices:
            send_data(choice)
            print(" Waiting for another player to choose")
            game_result = client.recv(1024).decode("utf-8")
            if "ready" not in game_result:
                print(game_result)
                if " You Win :)" in game_result:
                    score1 += 1
                elif " You Lose :(" in game_result:
                    score2 += 1 
            else:
                if " You Win :)" in game_result:
                    print(" You win :)")
                    score1 += 1
                elif " You Lose :(" in game_result:
                    print(" You Lose :(")
                    score2 += 1 
                else:
                    print(" It's a Draw!")
            i+=1 
        else:
            print(" Error: Invalid input, please try again")
        print(" Your current score : ")
        print(score1)
        
    if score2 < score1:
        print(" Congratulations! You are the Winner ")
    elif score1 < score2:
        print(" Sorry, you lose the game ")
    else:
        print(" Congratulations! It's a Draw ")

ready = False

while True:
    start = client.recv(1024).decode("utf-8")
    if not ready:
        if start == "ready":
            print(" Ready to play")
            print(" ██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░")
            print(" ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
            print(" ██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝")
            print(" ██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗")
            print(" ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║") 
            print(" ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝")
            print(" ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░")
            print(" ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗")
            print(" ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝")
            print(" ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗")
            print(" ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║")
            print(" ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝")
            print(" ###  Welcome to Rock Paper Scissor Multiplayer Game!  ###")
            print(" There will be FIVE rounds of game, Your choices >>> ")
            print(" [R] Rock ")
            print(" [P] Paper ")
            print(" [S] Scissors ")
            game()
            ready = True
    client.close()
    print (" ###  Thank You for playing with Us!  ###")
    print (" Connection closed")
    break
