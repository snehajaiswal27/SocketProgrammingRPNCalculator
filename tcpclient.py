import socket
import sys

# referenced https://realpython.com/python-sockets/#tcp-sockets to understand code structure 

OPERANDS = {"+", "-", "*", "/"}

def splitter(expression):

    tokens =[]
    curr = ""

    i = 0
    while i < len(expression):

        char = expression[i]

        if char.isdigit() or (char == '-' and (len(curr) == 0 or (tokens and tokens[-1] in OPERANDS))):
            curr += char
            i += 1

        elif (char in OPERANDS):
            if curr:
                tokens.append(curr)
                curr = ""
            tokens.append(char)
            i += 1

            while i < len(expression) and expression[i] in OPERANDS:
                tokens.append(expression[i])
                i += 1

            continue
        elif char.isspace():
            if curr:
                tokens.append(curr)
                curr = ""
            i += 1
        else:
            return []
        
    if curr in OPERANDS:
        tokens.append(curr)
        
    return tokens

def connect_server(hostname, port, expression):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #print("connecting")
        s.connect((hostname, port))
        #print("connected")

        tokens = splitter(expression)

        #print(tokens)

        if not tokens:
            print("Invalid expression", flush=True)
            return

        stack = []

        total = 0
        
        for token in tokens:

            #print("hi1")

            if token in OPERANDS:

                #print("hi2")

                if len(stack) < 2:
                    print("Invalid expression", flush=True)
                    return
                
                num1 = stack.pop()
                num2 = stack.pop()

                if not num1.lstrip('-').isdigit() or not num2.lstrip('-').isdigit():
                    print("Invalid expression", flush=True)
                    return
                
                expression = f"{num2} {num1} {token}"
                print(f"Sending operation: {expression}", flush=True)

                s.sendall(expression.encode())
                total = s.recv(1024).decode()

                if total == "Invalid expression":
                    print("Invalid expression", flush=True)
                    return
                else:
                    stack.append(total)
            else:
                stack.append(token)

        if len(stack) != 1:
            print("Invalid expression", flush=True)
            return

        print(f"Total: {total}", flush=True)


if __name__ == "__main__":
    
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    expression = sys.argv[3]

    connect_server(hostname, port, expression)