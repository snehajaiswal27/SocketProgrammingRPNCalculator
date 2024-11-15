import socket
import sys
from rpncalc import RPNCalculator

HOST = '127.0.0.1'

def start_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

        s.bind((HOST, port))

        print(f"Server started on port {port}. Accepting connections", flush = True)

        while True:

            data, addr = s.recvfrom(2048)

            data = data.decode()

            print(f"Received operation: {data}",flush=True)

            calc = RPNCalculator()
            result = calc.evaluate(data)

            s.sendto(str(result).encode(), addr)




if __name__ == "__main__":

    port = int(sys.argv[1])
    start_server(port)