import socket
host_ip = 'localhost'
port_no = 5000
def connect(host_ip,port_no):
	s=socket.socket()
	s.connect((host_ip, port_no))
	return s

def transfer_data(fname,s):
	while True:
		if fname == "exit":
			s.send(str.encode(fname))
			data=str(s.recv(2048).decode())
			print(data)
			break
		else :  
			f = open(fname,'rb')
			l = f.read(1024)
			print("data sending ", end =" ")
			while (l):
				print(".", end =" ")
				s.send(l)
				l = f.read(2048)
			f.close()
			s.send(str.encode("File transfer complete"))
			print("\n")

			while True:
				data = s.recv(1024)
				if str(data).find("File sent back from server") != -1:
					break
				print(data)
			print("File received back\n")
			fname= input("Enter another file name or type exit : ")
		
def main():
	s=connect(host_ip, port_no)
	fname=input('Enter file name')
	transfer_data(fname,s)
	s.close()

if __name__== "__main__":
    main()