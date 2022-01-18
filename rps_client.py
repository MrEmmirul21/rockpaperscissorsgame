import socket
import threading

host = '192.168.170.14'
port = 8888
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
except socket.error as e:
    print(str(e))

print(" Waiting for other player")
choices = ['R', 'P', 'S', "s", "p", "r"]   #set of choices
start = client.recv(512).decode("utf-8")
print(start)

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
print(" > [R] Rock ")
print(" > [S] Scissor ")
print(" > [P] Paper ")

for x in range(5):

    choice = input(" What is your choice ? >> ")
    while True:
        if choice in choices:
            client.send(choice.encode("utf-8"))
            break
        else:
            choice = input(" > Wrong input, try again >> ")

    result = client.recv(5500).decode("utf-8")
    print(result)
    print("Your current score: ")
    score = client.recv(5500).decode("utf-8")
    print(score)
    x += 1

finalR = client.recv(5500).decode("utf-8")
print(finalR)

client.close()
