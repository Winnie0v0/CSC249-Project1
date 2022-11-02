# Group member: Sophia Dai, Yujun Shen, Winnie Zong
# Citation: https://www.youtube.com/watch?v=NGLeprazvkM
# From this Youtube tutorial we learned simple multithreading technique
# and we managed to apply to the context of this assignment
import socket
import threading
import select

IP = "0.0.0.0"
PORT = 6789
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    # TCP connection set up
    
    # Citation: https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method
    # According to the report in console, when a tab is open/refreshed, 
    # the browser (Chrome) sends two requests to the server (set up two connections) 
    # with only one of them asking for the correct file.
    # In order to handle infinite wait during recv when given an incorrect request 
    # (which prevent the browser from displaying content until the server is down),
    # we set the connection to non-blocking and set up a timeout handler 
    # where the connection would go down after waiting for recv for more than 10 seconds.
    conn.setblocking(0)
    connected = True
    while connected:
        ready = select.select([conn], [], [], 10)
        if ready[0]:
            # Message was received and the key word was retrieved 
            msg = conn.recv(SIZE).decode(FORMAT)
            print(f"[ORIGINAL MESSAGE] {msg}")
            filename = msg.split()[1]
            f = open(filename[1:])
            print(f"[{addr}] {msg}")

            outputdata = f.read()
            # Send the connection message
            conn.send(bytes("HTTP/1.1 200 OK","UTF-8"))
            conn.send(outputdata.encode())
        else:
            break

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to server address: IP and Port
    server.bind(ADDR)
    # Allow server to listen to multiple connections
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        # Create a main thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()