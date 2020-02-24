import socket
import sys

#Create socket that uses IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket has been created.")
host = 'localhost'
port = 8000
try:
    print("Looking for '" + host + "' IPv4 address...")
    ip = socket.gethostbyname(host)
except Exception:
    print("Something went wrong, exiting...")
    sys.exit(0)
print("The IP address is " + ip)
print("Starting server on " + str(ip) + ":" + str(port))
s.bind((host, port))

s.listen(5)
print("Socket is now listening")
connection, address = s.accept()
print("Connected with '" + str(address[0]) + ":" + str(address[1]))

while True:
    data = connection.recv(1024)
    if not data:
        print("Closing connection with" + str(address[0]) + ":" + str(address[1]))
        connection.close()
        break
    print("Received from " + "(" + str(address[0]) + ":" + str(address[1]) + "): " + data.decode('utf-8'))
    if data:
        print("Sending data back to the client")
        connection.sendall(data)

print("Closing the socket...")
s.close()
        
        
