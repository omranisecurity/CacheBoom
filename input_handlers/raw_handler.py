import os.path
from core.scanner import scan

def raw_handler(raw_request, cookie, mode, thread, silent):
    
    if os.path.isfile(raw_request):
        with open(raw_request, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
        try:
            empty_line_index = lines.index('')
        except ValueError:
            empty_line_index = len(lines)

        first_line = lines[0] if lines else ''
        headers = lines[1:empty_line_index]
        body = lines[empty_line_index+1:] if empty_line_index+1 < len(lines) else []

        headers_dict = {}
        for header in headers:
            if ':' in header:
                key, value = header.split(':', 1)
                headers_dict[key.strip()] = value.strip()
        body = '\n'.join(body)
        
        method, path, protocol = first_line.split()
        host = headers_dict.get('Host')
        url = f"https://{host}{path}" #By default, requests are sent using the HTTPS protocol.
        
        #print(url, protocol, headers_dict, body, method, cookie, mode, thread, silent)
        scan(url, protocol, headers_dict, body, method, cookie, mode, thread, silent)
    
    else:
        print("File doesn't exist.")