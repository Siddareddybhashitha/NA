import socket
def client():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    sock = socket.socket()  # instantiate
    sock.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    while True:  
            if message == "Bye from Client":
                          sock.send(message.encode())
                          data = sock.recv(1024).decode()
                          print(data)
                          if(data == "Bye from Server Bhashitha"):
                                  break
                          else:
                                  message=input("Take another input")
            elif message == "Hello from Client":
                           sock.send(message.encode())
                           data= sock.recv(1024).decode()
                           print(data)
                           message=input("Take another input")
            else:
                           sock.send(message.encode())
                           data = sock.recv(1024).decode()
                           print(data)
                           message = input("Enter message")

    sock.close()  # close the connection
if __name__ == '__main__':
    client()