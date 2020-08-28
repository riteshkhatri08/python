import socket
print("Running")
serversocket= socket.socket()
serversocket.bind(("",7990))
serversocket.listen(1)
client,address=serversocket.accept()
print("connected to ",address   )
message="hello client"
client.send(message.encode())   
client.close()
print("Stopped")
