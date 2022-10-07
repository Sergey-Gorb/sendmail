import smtplib
import os
from email.mime.text import MIMEText


def send_mail():
    sender = ''
    password = ''
    server = smtplib.SMTP('', 587)
    reciever = ''
    text = '''
    
    '''
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(text, 'html')
        msg['Subject'] = ''
        server.sendmail(sender, reciever, msg.as_string())

        return "The message was sent successfully"

    except Exception as _ex:
        return _ex



