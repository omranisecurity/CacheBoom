#!/usr/bin/env python3

import argparse
from input_handlers.main_handler import loader
from utils.banner import show_banner

def main():
    parser = argparse.ArgumentParser(prog='CacheBoom!', description='A tool for detecting Web Cache Deception and Web Cache Poisoning vulnerabilities.', epilog='version: 0.8.0')
    parser.add_argument('-u', '--url', type=str, help="example: https://www.google.com")
    parser.add_argument('-r', '--raw_request', type=str, help="example: ~/raw_request.txt")
    parser.add_argument('-l', '--list', type=str, help="example: ~/urls.txt")
    parser.add_argument('-c', '--cookie', type=str, default=None ,help="example: name=value; name2=value2")
    parser.add_argument('-m', '--mode', choices=['cd', 'cp'], required=True, help="choose scan mode")
    parser.add_argument('-t', '--thread', type=int, default=10, help="number of threads to use (default: 10)")
    parser.add_argument('-s', '--silent', action='store_true', default=None, help="show only result in output")
    args = parser.parse_args()
    
    if not args.silent:
        show_banner()

    try:
        loader(
                url=args.url,
                raw_request=args.raw_request,
                list=args.list,
                cookie=args.cookie,
                mode=args.mode,
                thread=args.thread,
                silent=args.silent
            )
        
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user (Ctrl+C). Exiting...")

if __name__ == '__main__':
    main()