import socket
import sys  

host = 'www.google.com'

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Error: Socket')
    sys.exit()

print('# Getting remote IP address') 
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Website is down!')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , 80))

# Send data to remote server
print('# Sending data to server')
request = "GET / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request)
except socket.error:
    print 'Error: Socket'
    sys.exit()

# Receive data
print('# Receive data from server')
reply = s.recv(4096)

print reply
