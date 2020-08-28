import socket
import time
from threading import Thread
import sys

"""
print("trying connection")

#creating a socket
s= socket.socket()
#requesting connection on ip-127.0.0.1 and por number 7990
s.connect(('127.0.0.1', 7990))
print(s.recv(1024).decode())

#close the connection
s.close
"""

def checkConnection(conSocket):

    try:
        conSocket.send(str("server are you there ?").encode())
        return True
    except Error as err:
        
        print("exception : ",err)
        return False

def sendMessage(conSocket,senderName):
    while(checkConnection(conSocket)):
        time.sleep(5)
        msgSend= input("$pychat@console/"+senderName+" : ")
        conSocket.send(msgSend.encode())

def recvMessage(conSocket,senderName):
    while(checkConnection(conSocket)):
        msgRecv=conSocket.recv(1024).decode()
        print("$pychat@console/newMessage "+msgRecv)
        print("$pychat@console/"+senderName+" : ")
        time.sleep(5)
        

print(".....Welcome to pychat.....")
consoleName="$pychat@console :"
conSocket = socket.socket()
recvName=""
global client
#Input client Namee
clientName=input(consoleName+"Enter your name: ")

flag=True
while(flag):

    #input your choice
    choice= input(consoleName + "What do u wanna do? \nenter '1' to connect to friend   \nenter '2' to wait for a friend to connect \nenter '3' to exit.  \nYour choice : "  )

    if choice == '1':
        flag
        flag=False
        recvAdd= input(consoleName+"enter friends ip : ")
    
        print(consoleName,"connecting.....")
        # Trying a connection to the address
        client = conSocket.connect((recvAdd, 7990))
        print("Connected")
        #checking if we have successfully connected
        if ( checkConnection(client) ):
             print (consoleName,"connected successfully ")
        else:
            print(consoleName,"connection failed... Try Again")
            flag = True
            
            
    elif choice == '2':
       
        
        flag= False
        recvAdd= input(consoleName+"enter  your  ip  which your friend can connect to : ")
        print(consoleName,"Alright.. Let's wait for your friend to connect")
        conSocket.bind((recvAdd,7990))
        conSocket.listen(5)
        client=conSocket.accept()
        
        print(consoleName,"Connection accepted from :", client)
    elif choice == '3':
        sys.exit()
    else:
        print(consoleName,"Invalid Choice..Tray Again")
    
sendThread=Thread(target=sendMessage,args=(client,clientName),group=None)
recvThread=Thread(target=recvMessage,args=(client,clientName),group=None)
sendThread.start()
recvThread.start()                    




