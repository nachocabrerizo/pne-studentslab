from Seq1 import *
import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        clean_msg = msg.strip()

        x = clean_msg.split(" ")

        gene_list = ["AAAAAAAAAAAAAAAAAAAAAAAAA", "GGGGGGGGGGGGGGGGGGGGGGGGG", "CCCCCCCCCCCCCCCCCCCCCCCCC",
                     "TTTTTTTTTTTTTTTTTTTTTTTTT"]

        if x[0] == "PING":
            response = "OK!\n"

        if x[0] == "GET":
            if x[1] == "0":
                response = gene_list[0]
            elif x[1] == "1":
                response = gene_list[1]
            elif x[1] == "2":
                response = gene_list[2]
            elif x[1] == "3":
                response = gene_list[3]

        if x[0] == "INFO":
            response = ("The dna string is:", x[1], "The legth of the dna string is:", len(x[1]),)



        # -- Print the received message
        print(f"Message received: {msg}")


        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

