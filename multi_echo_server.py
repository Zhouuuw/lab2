import socket
import time
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024
#Question 5: What is returned by recv() from the server after it is done sending the HTTP request?
# if it is blank then break the loop
def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST,PORT))
        s.listen(2)
        while True:
            conn,addr = s.accept()
            p = Process(target = handle_echo, args=(addr,conn))
            #print("Conneted by ",addr)
            p.daemon = True
            p.start()
            #full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            #conn.sendall(full_data)
            #conn.close()

def handle_echo(addr,conn):
    print("Connect by", addr)

    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()


if __name__ == "__main__":
    main()

main()
