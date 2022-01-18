import socket
import threading

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
    print(" There will be FIVE rounds of game, Your choices >>> ")
    print(" >>> r = Rock ")
    print(" >>> s = Scissor ")
    print(" >>> p = Paper ")
    choice = input(" What is your choice ? >> ")
    if choice == "r" or choice == "s" or choice == "p":
        client.send(choice.encode("utf-8"))
        print(" Waiting for other player respond...")
        result = client.recv(1024).decode("utf-8")
        print(result)
        client.close()
    else:
        print(" Not correct input...")
        game()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.170.14'
port = 8888
try:
    client.connect((host, port))
    print(" Waiting for other player...")
except socket.error as e:
    print(str(e))
    
ready_to_play = False

while True:
    dataIn = client.recv(1024).decode("utf-8")
    if not ready_to_play:
        if dataIn == "READY_TO_PLAY":
            print(" Ready to play")
            game()
            ready_to_play = True
        
