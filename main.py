import socket
import sys
import threading  

URLS = []
args = [URLS]

def cycleSites(websites):
    '''cycles thru list of websites and runs wget for each
        Args:
            websites(arr<str>): array of websites to ping
    '''
    timer = threading.Timer(4.0, cycleSites, args)
    timer.daemon = True 
    timer.start()
    for site in websites:
        wget(site)

def main():
   cycleSites(URLS)
   while (1):
      host = raw_input("Enter the host URL (Type EXIT to exit, remove to remove): ")
      if (host == 'EXIT'):
         break
      if (host == 'remove'):
          host = raw_input("Enter the URL to remove: ")
          url = format_host(host)
          if URLS.count(url) == 1:
              URLS.remove(url)
              print("Removed " + url)
      else:
          url = format_host(host)
          print(url)
          if URLS.count(url) != 1:
              URLS.append(url)
              print("Added " + url)
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
