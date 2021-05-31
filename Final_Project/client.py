import json
import server
import http.client

SERVER = server
PARAMS = "http://127.0.0.1:8080/listSpecies?limit=8&json=1"

connection = http.client.HTTPConnection(SERVER)