# Group member: Sophia Dai, Yujun Shen, Winnie Zong
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# -------------
# Fill in start
# -------------

# Citation: https://www.youtube.com/watch?v=Lbfe3-v7yE0
# Youtube tutorial on python socket

# Task: Assign a port number
#       Bind the socket to server address and server port
#       Tell the socket to listen to at most 1 connection at a time

# Assign a port number
# Question: Why port 0000 doesn't work
# Answer: https://unix.stackexchange.com/questions/180492/is-it-possible-to-connect-to-tcp-port-0
# Asking to bind TCP on port 0 indicates a request to dynamically generate an unused port number
port = 6789

# Bind the socket to server address and server port

# Use localhost:
# host = gethostbyname(gethostname())
# print(host)
# serverSocket.bind((host, port))

# Use "":
# Question: How does empty string work for host?
# Answer: https://docs.python.org/3/library/socket.html
# Simply use 0.0.0.0
serverSocket.bind(("", port))

# Tell the socket to listen to at most 1 connection at a time
serverSocket.listen(1)

# -----------
# Fill in end
# -----------

while True:
    
    # Establish the connection
    print('Ready to serve...') 
    
    # -------------
    # Fill in start
    # -------------
    
    connectionSocket, addr = serverSocket.accept() # Task: Set up a new connection from the client
   
    # -----------
    # Fill in end
    # -----------

    try:
        
        # -------------
        # Fill in start
        # -------------
        
        # Question: When to use connection socket and when to use server socket?
        # Answer: connectionSocket is defined above 
        # and here we are trying to read the message it received so we are using connection socket
        message = connectionSocket.recv(1024) # Task: Receive the request message from the client
        print(message)

        # -----------
        # Fill in end
        # -----------
        
        # Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character
        f = open(filename[1:])
        
        # -------------
        # Fill in start
        # -------------

        # There will be a delay for styling to show up
        # read() instead of readline() to real the whole file at once
        outputdata = f.read() # Task: Store the entire contents of the requested file in a temporary buffer
        
        # -----------
        # Fill in end
        # -----------

        # -------------
        # Fill in start
        # -------------

        # Task: Send one HTTP header line into socket
        # Question: What exactly is a http header line
        # Answer: https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header
        # Need bytes and UTF-8
        connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n","UTF-8"))

        # -----------
        # Fill in end
        # -----------

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # -------------
        # Fill in start
        # -------------

        # Task: Send response message for file not found
        #       Close client socket
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","UTF-8"))
        connectionSocket.close()

        # -----------
        # Fill in end
        # -----------

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data