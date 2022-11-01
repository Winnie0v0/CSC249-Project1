# Project 1: DIY Webserver

_Attribution: this assignment is based on Webserver Lab from Computer Networking: a Top-Down Approach by Jim Kurose and Keith Ross. It was modified for use in CSC249: Networks at Smith College by R. Jordan Crouser in Fall 2022._

## Introduction
In this project, you will dig a bit deeper into the basics of socket programming for TCP connections in Python: how to create a socket, bind it to a specific address and port, as well as send and receive a HTTP packet. You will also learn some basics of HTTP header format.

## Phase 1:
You will develop a web server that handles one HTTP request at a time. Your web server should accept and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and then send the response directly to the client. If the requested file is not present in the server, the server should send an HTTP `404 Not Found` message back to the client.

### Support Code
The file `webserver.py` contains starter code for your Web server. Your task is to fill in code in the area marked with #Fill in start and #Fill in end in order to get your program to behave as described.

### Running	the	Server
- Put an HTML file (e.g., `HelloWorld.html`) in the same directory that the server is in. 
- Run the server program. 
- Determine the IP address of the host that is running the server (e.g., 128.238.251.26). 
- From another host, open a browser and provide the corresponding URL. For example: http://128.238.251.26:6789/HelloWorld.html where ‘HelloWorld.html’ is the name of the file you placed in the server directory. Note also the use of the port number after the colon. You need to replace this port number with whatever port you have used in the server code. In the above example, we have used the port number 6789. 
- The browser should then display the contents of `HelloWorld.html`. If you omit ":6789", the browser will assume port 80 and you will get the web page from the server only if your server is listening at port 80.
- Then try to get a file that is not present at the server. You should get a “404 Not Found” message.

## Phase 2
Currently, the web server handles only one HTTP request at a time. Implement a multithreaded server that is capable of serving multiple requests simultaneously. Using threading, first create a main thread in which your modified server listens for clients at a fixed port. When it receives a TCP connection request from a client, it will set up the TCP connection through another port and services the client request in a separate thread. There will be a separate TCP connection in a separate thread for each request/response pair.

## Phase 3
Instead of using a browser, write your own HTTP client to test your server. Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output. You can assume that the HTTP request sent is a GET method. The client should take command line arguments specifying the server IP address or host name, the port at which the server is listening, and the path at which the requested object is stored at the server.

The expected command format to run the client is as follows:
```client.py server_host server_port filename```

## Reflection
To run phase two, please run webserver2 and then connect to server via browser using method in phase1

To run phase three, please first run webserver2 and then run client.py with 0.0.0.0 as host ip, 6789 as port, and HelloWorld.html as filename.
