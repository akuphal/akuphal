import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10



def server(server_port,router_ip,router_port):
    server_1_ip = "127.0.0.1"
    server_1_port = 1240
    # create an INET, STREAMing socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
        # bind the socket to the host and its port
        
        serversocket.bind(('', server_port))
        
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # prepare for connection
        serversocket.listen(QUEUE_LENGTH)

        while True:
            # accept connections from outside
            (clientsocket, address) = serversocket.accept()

            with clientsocket:
                while True:
                    # receive data and print it out
                    data = clientsocket.recv(RECV_BUFFER_SIZE)
                    if not data: break
                    data = data.decode('utf-8')
                    data_list = data.split("~")
                    server_ip = data_list[1]
                    server_port = data_list[2]
                    print("data: " + data)
                    print("sip: " + server_ip)
                    print("sport: " + server_port)
                sys.stdout.flush()
    pass


def main():
    """TODO: CHANGE TO 3 ARGS, CLIENT PORT, ROUTER IP, ROUTER PORT"""
    if len(sys.argv) != 4:
        sys.exit("Usage: python server-python.py [Server Port] [Router IP] [Router Port] ")
    server_port = int(sys.argv[1])
    router_ip = sys.argv[2]
    router_port = int(sys.argv[3])
    server(server_port,router_ip,router_port)

if __name__ == "__main__":
    main()
