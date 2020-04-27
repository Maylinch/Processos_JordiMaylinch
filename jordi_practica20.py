# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
class Serve(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            f =  open(self.path[1:], 'rb')
            print('path ',self.path[1:])
            print("dbug")
            self.send_response(200)
            print("dbug")
            self.send_header('Content-type',        'image/jpg')
            print("dbug")
            self.end_headers()
            print("dbug")
            self.wfile.write(f.read())
            print("daaabug")
            f.close()


        except IOError:
            print("debug")
            print('path',',',self.path[1:])

            self.send_error(404,'file Not Found: %s -   ' %self.path[1:])

        self.envia()



    def envia(self):
        gmail_user ='jordimaylinch99@gmail.com'
        gmail_password ='nw3dsps4xb1'

        sent_from = gmail_user
        to = ['jordimaylinch99@gmail.com']
        subject = 'OMG Super Important Message'
        body = 'Hey, what\'s up?\n\n- You'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print(  'Email sent!')



httpd = HTTPServer(('localhost', 8080), Serve)
httpd.serve_forever()
