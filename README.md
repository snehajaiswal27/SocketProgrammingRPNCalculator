Network-Based Reverse Polish Notation (RPN) Calculator
======================================================

This project is a client-server application that demonstrates basic network programming concepts using TCP and UDP sockets. The RPN Calculator allows users to perform calculations in Reverse Polish Notation over a network. This project is designed to familiarize users with socket programming, client-server architecture, application-layer protocol design, and error handling.

Objectives
----------

*   **TCP and UDP Socket Usage**: Learn the creation and use of both TCP and UDP sockets to enable network communication.
    
*   **Client-Server Architecture**: Implement a client-server architecture for handling RPN calculations across a network.
    
*   **Application-Layer Protocol Design**: Design and implement a simple protocol for sending and receiving calculations between the client and server.
    
*   **Error Handling**: Manage network errors and implement basic recovery mechanisms to ensure reliable communication.
    

Project Details
---------------

The application supports calculations in Reverse Polish Notation (RPN), a mathematical notation in which operators follow their operands. For more information on RPN, see [Wikipedia](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

### Features

*   **TCP and UDP Versions**: The application includes both TCP and UDP implementations of the calculator, providing flexibility for different network environments.
    
*   **Error Recovery**: Basic error handling and recovery mechanisms are implemented to maintain connection integrity.
    
*   **Documentation**: Detailed documentation of the project’s design and implementation is included in the README.md file.
    

Running the RPN Calculator
--------------------------

To start the application, follow these steps to run the server and client programs. Note that you’ll need to start the server in a separate window before running the client.

### Command Conventions

*   **$**: Indicates the start of a command.
    
*   **#**: Indicates output (not part of the command).
    
*   _Italics_: Represents variable inputs.
    
*   xxx: Specifies whether to use "udp" or "tcp".
    

### Steps

Command: $ python3 xxxserver.py port

Output: # Server started on port port. Accepting connections

Command: $ python3 xxxclient.py hostname port expression

Output (on Client): # Sending operation: operation\_1

Output (on Server): # Received operation: operation\_1

...

Output (on Client): # Sending operation: operation\_n

Output (on Server): # Received operation: operation\_n

Output (on Client): # Total: final answer

Replace xxx with either "udp" or "tcp" depending on which protocol you want to use, and substitute hostname, port, expression, and operation\_n with your specific values.

### Example

Command: $ python3 tcpserver.py 8000

Output: # Server started on port 8000. Accepting connections

Command: $ python3 tcpclient.py 127.0.0.1 8000 "25 5 \* 60 +"

Output (on Client): # Sending operation: 25 5 \*

Output (on Server): # Received operation: 25 5 \*

Output (on Client): # Sending operation: 125 60 +

Output (on Server): # Received operation: 125 60 +

Output (on Client): # Total: 185
