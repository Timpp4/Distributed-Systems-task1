import socket
import sys
        

#Create socket that uses IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket has been created.")
#host = input("Give server address: ")
#port = int(input("Give server port: "))
#FOR TESTING PURPOSES
host = 'localhost'
port = 8000
try:
    ip = socket.gethostbyname(host)
    print("Trying to connect to '" + str(ip) + ":" + str(port))
    s.connect((host, port))
    print("Connected to " + str(ip) + ":" + str(port))
    print("Type 'quit' to disconnect from the server.")
except Exception:
    print("Something went wrong, exiting...")
    sys.exit(0)
    
    
        
while True:          
    message = input("What do you want to say?: ")
    if message == 'quit':
        print("Closing the connection...")
        s.close()
        break
    message = message.encode('utf-8')
    s.sendall(message)
    #Receive messages
    data = s.recv(1024)
    print(data.decode('utf-8'))
    

