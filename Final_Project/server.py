import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import jinja2

PORT = 8080

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

        else:
            pass


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