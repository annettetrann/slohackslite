import socket
import sys
import threading  
import re

URLS = []
args = [URLS]

def cycleSites(websites, thread_time):
    '''cycles thru list of websites and runs wget for each
        Args:
            websites(arr<str>): array of websites to ping
    '''
    timer = threading.Timer(thread_time, cycleSites, [URLS, thread_time])
    timer.daemon = True 
    timer.start()
    for site in websites:
        wget(site)

def main():
   thread_time = float(input('Enter the threading time in seconds: '))
   cycleSites(URLS, thread_time)
   while (1):
      '''Format of input URL should be either of the following:
         1) http://www.......
         2) http://..........
         3) https://www......
         4) https://.........
      '''
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
          if (url != None) and (URLS.count(url) != 1):
              URLS.append(url)
              print("Added " + url)
   return 0

def check_host_valid(host):
   regex = ("((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" +
         "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)")
   p = re.compile(regex)
   if (host == None):
      sys.stderr.write('Error: Invalid URL input "' + host + '"\n')
      return False
   if (re.search(p, host)):
      return True
   else:
      sys.stderr.write('Error: Invalid URL input "' + host + '"\n')
      return False 
    
def format_host(host):
   if not check_host_valid(host):
      return None
   formattedHost = 'www.'
   for i in range(len(host)):
      if host[i:i+3] == '://':
         i += 3
         if host[i:i+4] == 'www.':
            i += 4
         while (i != len(host)) and (host[i] != '/'):
            formattedHost += host[i]
            i += 1
         break
   return formattedHost

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
