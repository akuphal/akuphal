###############################################################################
# server-python.py
# Name: 
###############################################################################

import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10




def server(router_port):
    """TODO: HARD CODE FORWARDING TABLE"""
    server_1_ip = "127.0.0.1"
    server_1_port = 1240
    server_2_ip = "127.0.0.1"
    server_2_port = 1250
    forwarding_table = [(server_1_ip, server_1_port),(server_2_ip,server_2_port)]
    
    # create an INET, STREAMing socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
        # bind the socket to the host and its port
        serversocket.bind(('', router_port))
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # prepare for connection
        serversocket.listen(QUEUE_LENGTH)

        while True:
            # accept connections from outside
            (clientsocket, address) = serversocket.accept()
            #I believe this is the location that a statement connecting the router to the client needs to be placed

            with clientsocket:
                while True:
                    # receive data and print it out
                    data = clientsocket.recv(RECV_BUFFER_SIZE)
                    if not data: break
                    """TODO: OPEN MESSAGE, CHECK DESTINATION IP/PORT"""
                    data = data.decode('utf-8')
                    print("data: " + data)
                    data_list = data.split("~")
                    server_ip = data_list[1]
                    print("sip: " + server_ip)
                    server_port = data_list[2]
                    print("sport: " + server_port)
                    server_port = int(server_port)
                    
                    """TODO: NEW SOCKET, CONNECT TO CORRECT SERVER, SAME MSG OUT"""
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        #if forwarding_table.count((server_ip,server_port)) != 0: ##check forwarding table
                        s.connect((server_ip, server_port)) 
                        data = data.encode('utf-8')
                        sent = s.sendall(data)
                        if sent == 0:
                            raise RuntimeError("socket connection broken")
    pass


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Router Port]")
    router_port = int(sys.argv[1])
    server(router_port)

if __name__ == "__main__":
    main()
