import http.server
import socketserver
import http.client
import termcolor
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import jinja2
import json

PORT = 8080
SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

socketserver.TCPServer.allow_reuse_address = True

def read_template_html_file(filename):
    content = jinja2.Template(Path(filename).read_text())
    return content


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)


        if path_name == "/":
            contents = read_template_html_file("index.html").render()

        elif path_name == "/listSpecies":
            ENDPOINT = "info/species"
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", ENDPOINT + PARAMS)
            response = connection.getresponse().read().decode()
            limit = arguments["limit"][0]
            dictionary_response = json.loads(response)
            dictionary_values = dictionary_response.values()
            list_species =[]
            for dictionary in dictionary_values:
                for element in dictionary:
                    species = element["common_name"]
                    list_species.append(species)
            context = {}
            context["input_number"] = limit
            list_final_species = []
            try:
                integer_limit = int(limit)
            except ValueError:
                contents = read_template_html_file("error.html").render()

            for number in range(0,integer_limit):
                list_final_species.append(list_species[number])

            context["length"] = len(list_species)
            context["species_list"] = list_final_species
            contents = read_template_html_file("list_species.html").render(context=context)

        elif path_name == "/karyotype":
            species = arguments["specie"][0].replace(" ", "_")
            ENDPOINT = "info/assembly/" + species
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", ENDPOINT + PARAMS)
            response = connection.getresponse().read().decode()
            dictionary_response = json.loads(response)
            karyotype = dictionary_response.get("karyotype")
            context = {}
            context["list_karyotype"] = karyotype
            contents = read_template_html_file("karyotype.html").render(context=context)


        elif path_name == "/chromosomeLength":
            species = arguments["specie"][0].replace(" ", "_")
            ENDPOINT = "info/assembly/" + species
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", ENDPOINT + PARAMS)
            response = connection.getresponse().read().decode()
            dictionary_response = json.loads(response)
            list_possible_values = dictionary_response["top_level_region"]
            print(list_possible_values)
            context = {}
            contents = read_template_html_file("chromosome.html").render(context=context)

        else:
            contents = "Error"



        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

    # ------------------------
    # - Server MAIN program
    # ------------------------
    # -- Set the new handler
Handler = TestHandler

    # -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    print("Waiting for server")

        # -- Main loop: Attend the client. Whenever there is a new
        # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()