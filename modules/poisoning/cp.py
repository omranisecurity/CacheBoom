import requests, random, string, time
from utils.readfile import readfile
from colorama import Fore, Style

base_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0'}
custom_headers = readfile()
cacheboom_value = "cacheboom.com"

def random_string(length=4):
    chars = string.ascii_letters + string.digits
    return(''.join(random.choice(chars) for _ in range(length)))

def scan_cp(url, protocol, headers_dict, body, method, cookie, mode, thread, silent, output):
    max_requests_per_sec = thread if thread is not None else 10
    delay = 1.0 / max_requests_per_sec if max_requests_per_sec > 0 else 0

    for header_name in custom_headers:
        start_time = time.time()

        if headers_dict:
            test_headers = headers_dict.copy()
        else:
            test_headers = base_headers.copy()
            if header_name.lower() == "user-agent":
                continue

        test_headers[header_name] = cacheboom_value

        if cookie:
            test_headers['Cookie'] = cookie

        payload = "?" + random_string() + "=123"

        try:
            response = requests.request(
                method=method,
                url=url+payload,
                headers=test_headers,
                data=body
            )

            result = ""
            if (any("miss" in str(value) for value in response.headers.values()) and cacheboom_value in response.text) or cacheboom_value in response.text:
                result = f"[+] [VULNERABLE] | URL: {url+payload} | Header: {header_name} | Payload: {cacheboom_value}"
                print(Fore.GREEN + result + Style.RESET_ALL)
            else:
                result = f"[-] [Not vulnerable] URL: {url+payload} | Header: {header_name} | Payload: {cacheboom_value}"
                print(Fore.RED + result + Style.RESET_ALL)
            if output:
                with open(output, "a") as f:
                    f.write(result + "\n")

        except requests.RequestException as e:
            print(Fore.RED + f"[!] Error with header {header_name}: {e}" + Style.RESET_ALL)

        elapsed = time.time() - start_time
        if delay > elapsed:
            time.sleep(delay - elapsed)
