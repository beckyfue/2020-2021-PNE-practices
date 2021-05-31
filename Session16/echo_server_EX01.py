import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from jinja2 import Template

# Define the Server's port
PORT = 8080
HTML_ASSETS = "html"
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
def read_template_html(filename):
    template = Template(Path(filename).read_text())
    return template

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        print(self.path)
        if self.path == "/":
            contents = Path(HTML_ASSETS + '/form_1.html').read_text()
        elif self.path.startswith("/echo"):
            message = parse_qs(urlparse(self.path).query)['msg'][0]
            print(message)
            contents = read_template_html(HTML_ASSETS + '/template_jinja.html').render(msg=message)
        else:
            contents = Path('/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(str.encode(contents))))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return
# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

