import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8888
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

def game():
    global player1, player2
    if player1 != "" and player2 != "":
        if player1 == "r":
            if player2 == "r":
                sendtoall(" It's a Draw!")
            elif player2 == "s":
                sendto1(" You Win :)", players[0])
                sendto1(" You Lose :(", players[1])
            elif player2 == "p":
                sendto1(" You Lose :(", players[0])
                sendto1(" You Win :)", players[1])
                
        elif player1 == "s":
            if player2 == "s":
                sendtoall(" It's a Draw!")
            elif player2 == "p":
                sendto1(" You Win :)", players[0])
                sendto1(" You Lose :(", players[1])
            elif player2 == "r":
                sendto1(" You Lose :(", players[0])
                sendto1(" You Win :)", players[1])
                
        elif player1 == "p":
            if player2 == "p":
                sendtoall(" It's a Draw!")
            elif player2 == "r":
                sendto1(" You Win :)", players[0])
                sendto1(" You Lose :(", players[1])
            elif player2 == "s":
                sendto1(" You Lose :(", players[0])
                sendto1(" You Win :)", players[1])
        player1 = ""
        player2 = ""

def thread_handling(conn, currentPlayerID):
    for x in range(5):
        try:
            choice = conn.recv(1024).decode("utf-8")
            global player1, player2
            if choice:
                if choice == "r" or choice == "s" or choice == "p":
                    if currentPlayerID == 0:
                        player1 = choice
                        game()
                    if currentPlayerID == 1:
                        player2 = choice
                        game()
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
        print("Can't have more players...")
        break
