import threading
from wget import wget
 
def cycleSites(websites):
    '''cycles thru list of websites and runs wget for each
        Args:
            websites(arr<str>): array of websites to ping
        Returns:
            None
    ''' 
    timer = threading.Timer(3.0, cycleSites, args)
    timer.daemon = True 
    timer.start()
    for site in websites:
        wget(site)

websites = ["www.google.com", "www.thiswebsiteisdown.com"]
args = [websites]
cycleSites([])
while True:
    host = raw_input("Enter URL\n")
    if host == "exit":
        break
    else:
        websites.append(host)
