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

1.  bashCopy code$ python3 xxxserver.py \*port\*
    
    *   # Server started on port \*port\*. Accepting connections
        
2.  bashCopy code$ python3 xxxclient.py \*hostname port expression\*
    
    *   # Sending operation: \*operation\_1\*
        
    *   # Received operation: \*operation\_1\*
        
    *   ...
        
    *   # Sending operation: \*operation\_n\*# Received operation: \*operation\_n\*# Total: \*final answer\*
        

Replace xxx with either "udp" or "tcp" depending on which protocol you want to use, and substitute _hostname_, _port_, _expression_, and _operation\_n_ with your specific values.
