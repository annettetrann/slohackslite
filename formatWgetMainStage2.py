import socket
import sys  

def main():
   URLS = []
   while (1):
      host = raw_input("Enter the host URL (Type EXIT to exit): ")
      if (host == 'EXIT'):
         break
      url = format_host(host)
      URLS.append(url)
   for host_id in URLS:
      wget(host_id)
   return 0

def check_host_valid(host):
    for i in range(len(host)):
        if host[i: i +4 ] == 'www.':
            return True
    return False
    
def format_host(host):
    if not check_host_valid(host):
        return None
    formattedHost = ''
    for i in range(len(host)):
        if host[i:i+4] == 'www.':
            formattedHost += host[i:i+4]
            i += 4
            while (i != len(host)) and (host[i] != '/'):
                formattedHost += host[i]
                i += 1
    return formattedHost

def wget(host):
    """Pings the website. Prints contents if up.
    Args:
        host(str): website to ping
    Returns:
        int: 1 if website is down, 0 if website is up
    """
    if (host == None):
       sys.stderr.write('Error: Invalid URL input\n')
       return 1
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
