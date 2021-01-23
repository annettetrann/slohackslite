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
            while host[i] != '/':
                formattedHost += host[i]
                i += 1
    return formattedHost
