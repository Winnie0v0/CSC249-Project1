from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# -------------
# Fill in start
# -------------

# Task: Assign a port number
#       Bind the socket to server address and server port
#       Tell the socket to listen to at most 1 connection at a time

# Assign a port number
# TODO: Port 0000 doesn't work
port = 6789

# TODO: Why is there a delay for styling
host = gethostbyname(gethostname())
print(host)
serverSocket.bind((host, port))

# Bind the socket to server address and server port
# TODO: How does empty string work for host?
# serverSocket.bind(("131.229.194.249", port))

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
        
        # TODO: When to use connection socket and when to use server socket?
        message = connectionSocket.recv(1024) # Task: Receive the request message from the client

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
        outputdata = f.read() # Task: Store the entire contents of the requested file in a temporary buffer
        # -----------
        # Fill in end
        # -----------

        # -------------
        # Fill in start
        # -------------

        # Task: Send one HTTP header line into socket
        # TODO: What exactly is a http header line
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