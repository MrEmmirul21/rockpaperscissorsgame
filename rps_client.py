import socket
import time

host = '192.168.56.14'  #server
port = 8888
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    print("waiting for other player")
    start = client.recv(512).decode("utf-8")
    print(start)
    print(" > Choices : ")
    print(" > R = Rock. ")
    print(" > S = Scissors. ")
    print(" > P = Paper. ")
    choice = input(" > What is your choice  ? \n > ")
    client.send(choice.encode("utf-8"))
    end = client.recv(5500).decode("utf-8")
    print(end)
