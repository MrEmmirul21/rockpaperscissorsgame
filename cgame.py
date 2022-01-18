import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.170.14'
port = 5050
choices = ['R', 'P', 'S', "s", "p", "r"]
client.connect((host, port))
print(" Connected to game server...")

def send_data(data):
    client.send(data.encode("utf-8"))

def game():
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
    print(" [R] Rock ")
    print(" [P] Paper ")
    print(" [S] Scissors ")
    choice = input(" Rock/Paper/Scissors : ")
    
    if choice in choices:
        send_data(choice)
        print(" Waiting for another player to choose")
        result = client.recv(1024).decode("utf-8")
        if "reset" and "ready" not in result:
            print(result)
            client.close()
        else:
            if " You win :)" in result:
                print(" You win :)")
            else:
                print(" You Lose :(")    
    else:
        print(" Error: Invalid input, please try again")
        game()

ready = False

while True:
    start = client.recv(1024).decode("utf-8")
    if not ready:
        if start == "ready":
            print(" Ready to play")
            game()
            ready = True
    if start == "reset":
        game()
