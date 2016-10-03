import smtplib

import smtplib

def sendEMail(text):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("login", "pass")
    message = "\r\n".join([ \
        "From: от кого", \
        "To: кому", \
        "Subject: тема", \
        "", \
        "{}".format(text) \
        ])
    server.sendmail("от кого", "кому", message)
    server.quit()
