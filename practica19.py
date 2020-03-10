from http.server import BaseHTTPRequestHandler, HTTPServer

class Serve(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(file_to_open,'utf-8'))
        except:
            file_to_open = "Not Found"
            self.send_error(404,file_to_open)
            #self.wfile.write(bytes(file_to_open,'utf-8'))



httpd = HTTPServer(('localhost', 8080), Serve)
httpd.serve_forever()
