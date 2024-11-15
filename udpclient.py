import socket
import sys

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

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

        s.settimeout(2)

        tokens = splitter(expression)

        if not tokens:

            print("Invalid expression", flush=True)
            return

        stack = []
        
        for token in tokens:

            if token in OPERANDS:

                if len(stack) < 2:
                    print("Invalid expression", flush=True)
                    return
                
                num1 = stack.pop()
                num2 = stack.pop()

                if not num1.lstrip('-').isdigit() or not num2.lstrip('-').isdigit():
                    print("Invalid expression", flush=True)
                    return

                attempts = 0
                while attempts != 3:
                    try:
                        expression = f"{num2} {num1} {token}"
                        print(f"Sending operation: {expression}", flush=True)
                        s.sendto(expression.encode(), (hostname, port))
                        total, _ = s.recvfrom(2048)
                        total = total.decode()
                        break
                    except socket.timeout:
                        attempts += 1
                        if attempts == 3:
                            print("Error - No response after 3 attempts", flush=True)
                            return

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

        print(f"Total: {stack[0]}", flush=True)

        


if __name__ == "__main__":
    
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    expression = sys.argv[3]

    connect_server(hostname, port, expression)