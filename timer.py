import threading
from wget import wget
 
def cycleSites(websites):
    '''cycles thru list of websites and runs wget for each
        Args:
            websites(arr<str>): array of websites to ping
        Returns:
            None
    ''' 
    timer = threading.Timer(4.0, cycleSites, args)
    timer.daemon = True 
    timer.start()
    for site in websites:
        wget(site)

websites = []
args = [websites]
cycleSites([])
while True:
    host = raw_input("Enter URL\n")
    if host == "exit":
        break
    if host == "remove":
        re = raw_input("Enter site to remove\n")
        if websites.count(re) == 1:
            websites.remove(re)
            print("Removed " + re)
    else:
        if websites.count(host) == 0:
            websites.append(host)
