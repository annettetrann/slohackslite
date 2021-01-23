import socket
import sys  

def wget(host):
    """Pings the website. Prints contents if up.
    Args:
        host(str): website to ping
    Returns:
        int: 1 if website is down, 0 if website is up
    """
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
        return 1

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
    return 0
