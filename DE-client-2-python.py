import sys
import socket

SEND_BUFFER_SIZE = 2048
RECV_BUFFER_SIZE = 2048

def client(router_ip, router_port, server_ip, server_port):
    client_ip = server_ip
    client_port = 1230
    
    # create an INET, STREAMing socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # now connect to server
        """TODO: CONNECT TO ROUTER IP/PORT"""
        s.connect((router_ip, router_port))
        
        with open(0, "rb") as fd:
            while True:
                content = sys.stdin.buffer.raw.read(SEND_BUFFER_SIZE)
                if not content: break
                """TODO: APPEND SERVERIP/PORT TO MESSAGE"""
                content = content.decode('utf-8')
                content = content + "~" + server_ip + "~" + str(server_port) 
                sent = s.sendall(content.encode('utf-8'))
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                """TODO: WAIT FOR SERVER RESPONSE, THEN EXIT"""
                data = s.recv(RECV_BUFFER_SIZE)
                if not data: break
                sys.stdout.buffer.raw.write(data)
                sys.exit("Client exited")
            sys.stdout.flush()
    pass


def main():
    """TODO: CHANGE TO 4 ARGS: SERVER IP, SERVER PORT, ROUTER IP, ROUTER PORT """
    if len(sys.argv) != 5:
        sys.exit("Usage: python3 client-python.py [Server IP] [Server Port] [Router IP] [Router Port] < [message]")
    server_ip = sys.argv[1] 
    server_port = int(sys.argv[2])
    router_ip = sys.argv[3]
    router_port = int(sys.argv[4])
    client(router_ip, router_port, server_ip, server_port)

if __name__ == "__main__":
    main()
