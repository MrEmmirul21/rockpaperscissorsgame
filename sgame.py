import socket
import threading

def send1(data, currentPlayer):
    for player in players:
        if currentPlayer == player:
            player.sendall(data.encode("utf-8"))
            
def sendall(data):
    for player in players:
        player.send(data.encode("utf-8"))
        
def thread_handling(conn, currentPlayerID):
    while True:
        try:
            choice = conn.recv(1024).decode("utf-8")
            global player1, player2
            if currentPlayerID == 0:
                player1 = choice
                game()
            elif currentPlayerID == 1:
                player2 = choice
                game()
        except:
            global playerID
            print("Player Disconnected: " + str(currentPlayerID))
            players.pop(currentPlayerID)
            playerID = currentPlayerID
            break
            
def game():
    global player1, player2
    if player1 == "r":
        if player2 == "s":
            send1("You Win!", players[0])
            send1("You Lose!", players[1])
        elif player2 == "p":
            send1("You Lose!", players[0])
            send1("You Win!", players[1])
                
    elif player1 == "s":
        if player2 == "p":
            send1("You Win!", players[0])
            send1("You Lose!", players[1])
        elif player2 == "r":
            send1("You Lose!", players[0])
            send1("You Win!", players[1])
                
    elif player1 == "p":
        if player2 == "r":
            send1("You Win!", players[0])
            send1("You Lose!", players[1])
        elif player2 == "s":
            send1("You Lose!", players[0])
            send1("You Win!", players[1])
            
    elif player1 == player2:
        sendall("IT'S A DRAW!!")
    
    player1 = ""
    player2 = ""           

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",8888))
s.listen(3)

players = []
playerID = 0
player1 = ""
player2 = ""

print("Waiting for players to join")

while True:
    if playerID < 3:
        conn, addr = s.accept()
        print("Player connected from: " + str(addr))
        players.append(conn)
        thread = threading.Thread(target=thread_handling, args=(conn, playerID))
        thread.start()
        
        if len(players) == 2:
            sendall("READY_TO_PLAY")

        playerID += 1
    else:
        print("Can't have more players...")
        break
