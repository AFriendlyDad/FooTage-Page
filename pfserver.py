import http.server
import socketserver
import os
import urllib
import cgi

path = os.getcwd()
files = os.listdir(path)
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'mywebpage.html'
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Black Lives Matter</title></head></html>".encode("utf-8"))
        self.wfile.write("<body style='background-color:Black;'>".encode("utf-8"))      
        self.wfile.write("<style> .oneline { width: 19%; height: 98%; border: solid 1px #ccc; display: inline-block; overflow-y: scroll;} .videoframe { width: 80%; height: 98%; border: solid 1px #ccc; display: inline-block; overflow-y: scroll;}</style>".encode("utf-8"))
        self.wfile.write("<div class='oneline'><p>".encode("utf-8"))
        for name in files:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
                # Note: a link to a directory displays with @ and links with /
            self.wfile.write(("<ul><a href='http://192.168.0.4:9001/" + name + "' target='clips'>" + name + "</a></ul>").encode("utf-8"))
        self.wfile.write("""</p></div><div scrolling='no' class="videoframe"><iframe scrolling='no' name='clips' width=98% height=98%><p>hello</p><video src="http://192.168.0.4:9001/2020-06-22%2021-33-43.mp4" autoplay=true controls=true ></video></iframe></div></n></body>""".encode("utf-8"))
        #return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 9000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
