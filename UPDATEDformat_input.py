def check_host_valid(host):
    start = 0
    extCount = 0
    for i in range(len(host)):
        if host[i: i +4 ] == 'www.':
            start = i+4
    for i in range(start, len(host)):
        if host[i] == '.':
            i += 1
            while (i != len(host)) and (host[i] != '/'):
                extCount += 1
                i += 1
    if (extCount != 2) and (extCount != 3):
        return False
    return True
    
def format_host(host):
    if not check_host_valid(host):
        return None
    formattedHost = 'www.'
    for i in range(len(host)):
        if host[i:i+4] == 'www.':
            i += 4
        while (i != len(host)) and (host[i] != '/'):
            formattedHost += host[i]
            i += 1
        break
    return formattedHost
