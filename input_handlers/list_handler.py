import os.path
from core.scanner import scan
from urllib.parse import urlparse
from utils.validator import url_validator

def list_handler(list, cookie, mode, thread, silent):
    if os.path.isfile(list):
        with open(list, "r") as file:
            urls = file.read().splitlines() 

            for url in urls:
                if url_validator(url):
                    parsed_url = urlparse(url)
                    protocol = parsed_url.scheme

                    headers_dict = None
                    body = None
                    method = "GET"
                    
                    scan(url, protocol, headers_dict, body, method, cookie, mode, thread, silent)
                else:
                    print(f"[~] [The URL is not valid] | URL: {url}")
        
    else:
        print("File doesn't exist.")
