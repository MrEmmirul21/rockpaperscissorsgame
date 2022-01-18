import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",8888))
print("Waiting for players to join")
s.listen(3)

# Keeping track of players
players = []
playerid = 0
player1 = ""
player2 = ""
score1 = 0
score2 = 0

# Send data to specific player
def dataplayer(data, currentPlayer):
    for player in players:
        if currentPlayer == player:
            player.sendall(data.encode("utf-8"))

# Send data to all players
def dataAll(data):
    for player in players:
        player.send(data.encode("utf-8"))


def game():
    global player1, player2, score1, score2

    if player1 == "r":
        if player2 == "r":
            dataAll("IT'S A DRAW!!")
        if player2 == "s":
            dataplayer("You Win!", players[0])
            score1 += 1
            dataplayer(score1, players[0])
            dataplayer("You Lose!", players[1])
            dataplayer(score2, players[1])
        if player2 == "p":
            dataplayer("You Lose!", players[0])
            dataplayer(score1, players[0])
            dataplayer("You Win!", players[1])
            score2 += 1
            dataplayer(score2, players[1])

    if player1 == "s":
        if player2 == "s":
            dataAll("IT'S A DRAW!!")
        if player2 == "p":
            dataplayer("You Win!", players[0])
            score1 += 1
            dataplayer(score1, players[0])
            dataplayer("You Lose!", players[1])
            dataplayer(score2, players[1])
        if player2 == "r":
            dataplayer("You Lose!", players[0])
            dataplayer(score1, players[0])
            dataplayer("You Win!", players[1])
            score2 += 1
            dataplayer(score2, players[1])

    if player1 == "p":
        if player2 == "p":
            dataAll("IT'S A DRAW!!")
        if player2 == "r":
            dataplayer("You Win!", players[0])
            score1 += 1
            dataplayer(score1, players[0])
            dataplayer("You Lose!", players[1])
            dataplayer(score2, players[1])
        if player2 == "s":
            dataplayer("You Lose!", players[0])
            dataplayer(score1, players[0])
            dataplayer("You Win!", players[1])
            score2 += 1
            dataplayer(score2, players[1])
    player1 = ""
    player2 = ""

def winner():
    global player1, player2, score1, score2

    if score1 > score2:
        dataplayer(" You are the Winner! congratulations :) ", players[0])
        dataplayer(" Sorry, You lose the game :( ", players[1])
    elif score2 > score1:
        dataplayer(" Sorry, You lose the game :( ", players[0])
        dataplayer(" You are the Winner! congratulations :) ", players[1])
    else:
        dataAll(" It's a draw! congratulations to both players ")

# Thread handling
def thread_handling(conn, id):
    while True:
        try:
            for x in range(5):
                choice = conn.recv(1024).decode("utf-8")
                global player1, player2
                if id == 0:
                    player1 = choice
                    game()
                if id == 1:
                    player2 = choice
                    game()
                x += 1
            winner()
        except:
            global playerid
            print("Player Disconnected: " + str(id))
            players.pop(id)
            playerid = id
            break

# Handling incoming connections
while True:
    if playerid < 3:
        conn, addr = s.accept()
        print("Player connected from: " + str(addr))
        players.append(conn)

        # Threading
        thread = threading.Thread(target=thread_handling, args=(conn, playerid))
        thread.start()
        if len(players) == 2:
            dataAll(" Game is starting ...")
        playerid += 1
    else:
        print("Cannot accept more players")
        break
