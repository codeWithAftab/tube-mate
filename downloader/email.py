import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def emailWithAttach(to,sub,filename="",body=""):
        fromaddr = "aftabWisher0@gmail.com"
        password = "xtnjqbmocjvaphal"
        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr
        msg['To'] = to
        msg['Subject'] = sub
        try:
         # string to store the body of the mail
        # attach the body with the msg instance
                msg.attach(MIMEText(body,'html'))
        except Exception as e:
                print(e)
        
        try:
        # open the file to be sent
                attachment = open(filename, "rb")
        # instance of MIMEBase and named as p
                p = MIMEBase('application', 'octet-stream')
                # To change the payload into encoded form
                p.set_payload((attachment).read())
                # encode into base64
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                # attach the instance 'p' to instance 'msg'
                msg.attach(p)
        except Exception as e:
                print(e)
        # creates SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr,password)
        # Converts the Multipart msg into a string
        text = msg.as_string()
        server.send_message(msg)
        server.quit()
