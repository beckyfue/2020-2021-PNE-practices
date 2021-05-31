import json
import http.client

PORT = 8080
SERVER = "127.0.0.1"
conn = http.client.HTTPConnection(SERVER, PORT)


def client(ARGUMENTS, PATH_NAME):
        conn.request("GET", PATH_NAME + ARGUMENTS)
        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # -- Read the response's body
        data1 = r1.read().decode("utf-8")
        # -- Print the received data
        data = json.loads(data1)
        return data


try:
    ARGUMENTS = "?limit=8&json=1"
    PATH_NAME = "/listSpecies"
    data = client(ARGUMENTS, PATH_NAME)
    list_names = " "
    for name in data["species_list"]:
        list_names = list_names + name + ", "
    print("The total number of species in the ensemble is: ", data["length"])
    print("The limit you have selected is: ", data["input_number"])
    print("The names of the species are", list_names)

except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()


