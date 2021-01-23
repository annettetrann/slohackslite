import socket
import sys  

def wget(host):
    """Pings the website. Prints contents if up.
    Args:
        host(str): website to ping
    Returns:
        int: 1 if website is down, 0 if website is up
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        sys.stderr.write('Error: Socket\n')
        sys.exit()

    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        sys.stderr.write('Website ' + host + ' is down!\n')
        return 1

    return 0
