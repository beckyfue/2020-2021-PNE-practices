import socket
from P3 import server_utils

list_sequences = ["ACGTTTTGGAAAAACTGA", "AGTTTTCCCAA", "TTGCAGAAGTC", "GGGGGCCCCCTTTTTAAAAA", "CCTTGGTTGAACAACCGT"]
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Configure the Server's IP and PORT
PORT = 8082
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
count_connections = 0
client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT:" + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)
    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    formated_message = server_utils.format_command(msg)
    print(formated_message)
    formated_message = formated_message.split(" ")
    if len(formated_message) == 1:
        command = formated_message[0]
    else:
        command = formated_message[0]
        argument = formated_message[1]
    if command == "PING":
        server_utils.ping()
        response = "OK!"
        cs.send(str(response).encode())
    elif command == "GET":
        server_utils.print_colours(("Get", "yellow"))
        response = list_sequences[int(argument)]
        print(response)
        cs.send(response.encode())
    else:
        response = "Not available command"
        cs.send(str(response).encode())
    # -- Close the data socket
    cs.close()
