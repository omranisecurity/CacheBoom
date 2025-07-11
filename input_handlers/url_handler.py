from urllib.parse import urlparse
from utils.validator import url_validator
from core.scanner import scan

def url_handler(url, cookie, mode, thread, silent, output):
    if url_validator(url):
        parsed_url = urlparse(url)
        protocol = parsed_url.scheme

        headers_dict = None
        body = None
        method = "GET"
        
        scan(url, protocol, headers_dict, body, method, cookie, mode, thread, silent, output)
    else:
        print(f"[~] [The URL is not valid] | URL: {url}")