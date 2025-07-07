import random
import string
import requests
from colorama import Fore, Style
import threading
import time
from queue import Queue

def random_string(length=4):
    chars = string.ascii_letters + string.digits
    return(''.join(random.choice(chars) for _ in range(length)))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0'
    }

special_chars = [
    "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
    "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~",
    "%21", "%22", "%23", "%24", "%25", "%26", "%27", "%28", "%29", "%2A", "%2B", "%2C", "%2D", "%2E", "%2F",
    "%3A", "%3B", "%3C", "%3D", "%3E", "%3F", "%40", "%5B", "%5C", "%5D", "%5E", "%5F", "%60", "%7B", "%7C", "%7D", "%7E"
    ]

file_extensions = [
    ".JS", ".CSS", ".EJS",
    ".JPG", ".JPEG", ".PNG", ".GIF", ".SVG", ".WEBP", ".BMP", ".TIFF", ".TIF", ".ICO", ".EPS", ".SVGZ", ".PICT",
    ".PDF", ".DOCX", ".DOC", ".XLSX", ".XLS", ".PPTX", ".PPT", ".CSV",
    ".TTF", ".OTF", ".WOFF", ".WOFF2", ".EOT",
    ".EXE", ".APK", ".DMG", ".ISO", ".BIN", ".CLASS", ".JAR", ".PS",
    ".MP4", ".AVI", ".MKV", ".WEBM", ".SWF", ".AVIF",
    ".MP3", ".OGG", ".FLAC", ".MIDI", ".MID", ".PLS",
    ".ZIP", ".RAR", ".7Z", ".GZ", ".BZ2", ".ZST", ".TAR"
    ]

payloads = {}

method = "GET"

def scan_cd(url, protocol, headers_dict, body, method, cookie, mode, thread, silent):
    if url[-1] != '/':
        url += '/'

    try:
        response1 = requests.request(method, url, headers=headers_dict, data=body)
        status_code1 = response1.status_code
        content_length1 = response1.headers.get('Content-Length')

        found = threading.Event()
        task_queue = Queue()
        interval = 1.0 / thread  # How much delay between each request

        def worker():
            while not task_queue.empty() and not found.is_set():
                test_url, baseline_code, baseline_length, payload = task_queue.get()
                try:
                    response = requests.request(method, test_url, headers=headers_dict, data=body)
                    status_code = response.status_code
                    content_length = response.headers.get('Content-Length')
                    cacheable = any("miss" in str(v).lower() for v in response.headers.values())

                    if (status_code == baseline_code) and (content_length == baseline_length) and cacheable:
                        found.set()
                        print(Fore.GREEN +
                            f"""[+] Vulnerable:
First Request | Status Code: {baseline_code} | Content Length: {baseline_length}
URL: {url}
---------------------------------------
Second Request | Status Code: {status_code} | Content Length: {content_length} | Payload: {payload}
URL: {test_url}
---------------------------------------""" + Style.RESET_ALL)
                    else:
                        if not silent:
                            print(f"[-] Not Vulnerable: {test_url}")
                except requests.RequestException as e:
                    print(f"Error during request: {e}")
                finally:
                    task_queue.task_done()
                    time.sleep(interval)  # Control request rate

        # STEP 1: Test with Extensions
        for ext in file_extensions:
            payload = random_string() + ext.lower()
            payloads[payload] = payload
            test_url = url + payload
            task_queue.put((test_url, status_code1, content_length1, payload))

        threads = []
        for _ in range(thread):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()
            threads.append(t)

        task_queue.join()

        # If nothing is found, go to the second stage
        if not found.is_set():
            if url.endswith('/'):
                url = url[:-1]

            response3 = requests.request(method, url, headers=headers_dict, data=body)
            status_code3 = response3.status_code
            content_length3 = response3.headers.get('Content-Length')

            exts = file_extensions.copy()
            random.shuffle(exts)

            for idx, spec_char in enumerate(special_chars):
                ext = exts[idx % len(exts)]
                payload = spec_char + random_string() + ext.lower()
                payloads[payload] = payload
                test_url = url + payload
                task_queue.put((test_url, status_code3, content_length3, payload))

            for _ in range(thread):
                t = threading.Thread(target=worker)
                t.daemon = True
                t.start()
                threads.append(t)

            task_queue.join()

        if not found.is_set():
            print("[-] Not Vulnerable to Cache Deception")

    except requests.RequestException as e:
        print(f"Error during request: {e}")
