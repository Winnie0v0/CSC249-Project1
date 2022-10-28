import socket
import sys

IP = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    # msg = 'GET /filename HTTP/1.1\r\n\r\n' sys.argv[3]
    msg = 'GET /'+sys.argv[3] + ' HTTP/1.1\r\n'
    # sys.argv[3]
    client.send(msg.encode(FORMAT))

    while True:
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()