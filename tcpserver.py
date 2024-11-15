import socket
import sys
from rpncalc import RPNCalculator

# referenced https://realpython.com/python-sockets/#tcp-sockets to understand how to code this 

HOST = '127.0.0.1' # connect to 127.0.0.1 by default

def start_server(port): # the port is passed in

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        #print("hi")

        s.bind((HOST, port))

        s.listen()

        print(f"Server started on port {port}. Accepting connections", flush = True)

        while True: # loop to accept connections

            conn, _ = s.accept()

            with conn:
                
                calc = RPNCalculator()

                while True:

                    data = conn.recv(1024).decode() # needs to be string for calc

                    if not data:
                        break

                    print(f"Received operation: {data}", flush = True)

                    result = calc.evaluate(data)

                    conn.sendall(str(result).encode()) # convert back to bytes

if __name__ == "__main__":

    port = int(sys.argv[1])
    start_server(port)