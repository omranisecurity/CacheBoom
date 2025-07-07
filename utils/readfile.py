def readfile():
    headers_dict = {}

    with open('wordlists/headers.txt', 'r') as file:
        for line in file:
            key = line.strip()
            if key:
                headers_dict[key] = "cacheboom.com"

    return headers_dict
