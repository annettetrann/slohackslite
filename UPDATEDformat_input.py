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
