import socket, time, sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 102

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(" ")
        sys.exit()

    return remote_ip

def main():

    host = "www.google.com"
    port = 80
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_start:
        print("starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        proxy_start.bind((HOST,PORT))
        proxy_start.listen(1)
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by",addr)
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_end:
                print('Connecting to Google')
                remote_ip = get_remote_ip(host)

                proxy_end.connect((remote_ip,port))

                send_full_data = conn.recv(BUFFER_SIZE)
                print(f"sending revieved data{send_full_data} to google")
                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(BUFFER_SIZE)
                print(f"Sending recieved data {data} to client")
                conn.send(data)
            
            conn.close()

if __name__ == "__main__":
    main()
