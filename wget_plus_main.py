import socket
import sys  

def main():
   URLS = []
   while (1):
      host = raw_input("Enter the host URL (Type EXIT to exit): ")
      if (host == 'EXIT'):
         break
      URLS.append(host)
   for host_id in URLS:
      wget(host_id)
   return 0

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
    print('Succesful ping @ ' + host + '!')
    return 0

if __name__ == "__main__":
   sys.exit(main())
