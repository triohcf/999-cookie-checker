import requests,threading,os
from colorama import Fore
os.system("cls")

cookies = open("cookies.txt").read().splitlines()

print(f'''{Fore.RED}
 █████╗  █████╗  █████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
╚██████║╚██████║╚██████║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
 ╚═══██║ ╚═══██║ ╚═══██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 █████╔╝ █████╔╝ █████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚════╝  ╚════╝  ╚════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                    Made by Vision#1420 | Edited By TrioHCF#0999                    
{Fore.WHITE}''')
threads = int(input(f"{Fore.WHITE}[{Fore.RED}999 Checker{Fore.WHITE}] {Fore.WHITE}Threads: "))

class Checker():
    def __init__(self,cookie):
        self.ses = requests.Session()
        self.ses.cookies['.ROBLOSECURITY'] = cookie
        robux=self.ses.get("https://api.roblox.com/currency/balance")
        if robux.status_code == 200:
            robux = robux.json()['robux']
            if robux > 0:
                print(f"{Fore.WHITE}[{Fore.RED}999 Checker{Fore.WHITE}] {Fore.GREEN}Valid Cookie with {Fore.WHITE}{robux}{Fore.LIGHTBLACK_EX} ROBUX")
                open("robux_valid.txt","a").write(f"{cookie}\n")
            else:
                print(f"{Fore.WHITE}[{Fore.RED}999 Checker{Fore.WHITE}] {Fore.GREEN}Valid Cookie")
                open("valid.txt","a").write(f"{cookie}\n")
        else:
                print(f"{Fore.WHITE}[{Fore.RED}999 Checker{Fore.WHITE}] {Fore.RED}Invalid Cookie{Fore.WHITE}")

def thread():
    while cookies:
        try:
            cookie = cookies.pop()
            Checker(cookie)
        except Exception as e:
            print(f"{Fore.WHITE}[{Fore.RED}999 Checker{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Error has occurred, it has been stored in {Fore.WHITE}errors.txt")
            open("errors.txt","a").write(f"{str(e)}\n")

for _ in range(threads):
    threading.Thread(target=thread).start()
