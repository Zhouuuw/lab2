# CMPUT404 - lab2 TCP socket

instruction: https://uofa-cmput404.github.io/lab-2-tcp-proxy.html


##  Question 1: How do you specify a TCP socket in Python?
##  When Creating a socket, specify the parameter "socket.SOCK_STREAM" 

## Question 2: What is the difference between a client socket and a server socket in Python?
## A client server is for sending request and waiting to recieve response from servers.
## A servers socket is used to listening to any requests from client and give responds.

## Question 3: How do we instruct the OS to let us reuse the same bind port?
## A socket flag, SO_REUSEADDR is set to in function call s.setsockopt

## Question 4: What information do we get about incoming connections?
## In the incoming connection, we can see the addr returning by function socket.accept()

## Question 5: What is returned by recv() from the server after it is done sending the HTTP request?
## Empty String.
