import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5050
s.bind((host, port))
s.listen(3)
print("Waiting for another player to join")

players = []
playerID = 0
player1 = ""
player2 = ""

def sendto1(data, currentPlayer):
    for player in players:
        if currentPlayer == player:
            player.sendall(data.encode("utf-8"))

def sendtoall(data):
    for player in players:
        player.send(data.encode("utf-8"))

def games():
    global player1, player2
    if player1 == "r":
        if player2 == "s":
            sendto1(" You win :)", players[0])
            sendto1(" You Lose :(", players[1])
        elif player2 == "p":
            sendto1(" You Lose :(", players[0])
            sendto1(" You win :)", players[1])
                
    elif player1 == "s":
        if player2 == "p":
            sendto1(" You win :)", players[0])
            sendto1(" You Lose :(", players[1])
        elif player2 == "r":
            sendto1(" You Lose :(", players[0])
            sendto1(" You win :)", players[1])
                
    elif player1 == "p":
        if player2 == "r":
            sendto1(" You win :)", players[0])
            sendto1(" You Lose :(", players[1])
        elif player2 == "s":
            sendto1(" You Lose :(", players[0])
            sendto1(" You win :)", players[1])
            
    elif player1 == player2:
        sendtoall("IT'S A DRAW!!!")
        player1 = ""
        player2 = ""
        time.sleep(0.5)
        sendtoall("reset")

def thread_handling(conn, currentPlayerID):
    while True:
        try:
            choice = conn.recv(1024).decode("utf-8")
            global player1, player2
            if choice:
                if choice == "r" or choice == "s" or choice == "p":
                    if currentPlayerID == 0:
                        player1 = choice
                        games()
                    if currentPlayerID == 1:
                        player2 = choice
                        games()
                else:
                    conn.send("\nError: Invalid input.".encode("utf-8"))
        except:
            global playerID
            print("Player Disconnected: " + str(currentPlayerID))
            players.pop(currentPlayerID)
            playerID = currentPlayerID
            break

while True:
    if playerID < 3:
        conn, addr = s.accept()
        print("Player connected from: " + str(addr))
        players.append(conn)
        thread = threading.Thread(target=thread_handling, args=(conn, playerID))
        thread.start()
        
        if len(players) == 2:
            sendtoall("ready")

        playerID += 1
    else:
        break
