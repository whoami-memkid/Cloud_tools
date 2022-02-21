#!/usr/bin/env python3
import requests, xml.etree.ElementTree as ET
import sys

def usage():
    print("./cloud_snake.py -r <region> -w <wordlist>")
    print("Tool for checking AWS s3 buckets using a wordlist")
    print("-r: region US, EU, AF, AP, CA, SA")
    print("-w: wordlist")
    exit()

def main():

    if len(sys.argv) == 1:
        usage()

    args = sys.argv
    
    region = "US"
    wordlist = ""
    for i in args:
        if '-r' in i:
            tracker = args.index(i)
            region = args[tracker + 1]

        if '-w' in i:
            tracker = args.index(i)
            wordlist = args[tracker + 1]
    

    if region == "US":
        with open(wordlist, 'r+', encoding="utf8") as f:
            for line in f:
                token = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
                for item in token:
                    url = 'https://s3.{}.amazonaws.com/{}'.format(item, line).strip()
                    x = requests.get(url)
                    print(url, "-", x.status_code)
                    if x.status_code == 404 or x.status_code == 200:
                        break
    
    if region == "EU":
        with open(wordlist, 'r+', encoding="utf8") as f:
            for line in f:
                token = ["eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-north-1"]
                for item in token:
                    url = 'https://s3.{}.amazonaws.com/{}'.format(item, line).strip()
                    x = requests.get(url)
                    print(url, "-", x.status_code)
                    if x.status_code == 404 or x.status_code == 200:
                        break

    exit()

if __name__ == "__main__":
    main()
