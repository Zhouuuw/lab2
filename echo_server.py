## 404 lab
## Question 2: What is the difference between a client socket and a server socket in Python?
## A client server is for sending request and waiting to recieve response from servers.
## A servers socket is used to listening to any requests from client and give responds.

## Question 3: How do we instruct the OS to let us reuse the same bind port?
## A socket flag, SO_REUSEADDR is set to in function call s.setsockopt

## Question 4: What information do we get about incoming connections?
## In the incoming connection, we can see the addr returning by function socket.accept()

## Question 5: What is returned by recv() from the server after it is done sending the HTTP request?
## Empty String.

import socket
import time

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
            print("Conneted by ",addr)
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()

main()
