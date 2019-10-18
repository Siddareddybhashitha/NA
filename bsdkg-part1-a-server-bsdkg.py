import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    sock = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    sock.bind((host, port))  # bind host address and port together
    sock.listen(1)
    conn, addr = sock.accept()  # accept new connection
    print("Connection from: " + str(addr))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if data == "Bye from Client-Bhashitha":
                print(data)
                conn.send(str.encode("Bye from Server-Bhashitha"))
                break
        elif data == "Hello from Client-Bhashitha":
                  print(data)
                  conn.send(str.encode("Hello from Server-Bhashitha"))
        else:
                  print(data)
                  conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection
if __name__ == '__main__':
    server_program()
