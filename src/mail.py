from email.mime.text import MIMEText
import smtplib
from src import Log

class Mail:
    def init(sender, password, receiver):
        global mail_user, mail_password, to, subject, body
        
        mail_user = sender
        mail_password = password
        to = receiver
        body = ""

        subject = 'Weather status update!'

    def addContent(content):
        global body
        body += content + "\n"

    def send():
        email_text = MIMEText(body)
        email_text['Subject'] = subject
        email_text['From'] = mail_user
        email_text['To'] = to

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(mail_user, mail_password)
            smtp_server.sendmail(mail_user, to, email_text.as_string())
            smtp_server.close()
            print ("Email sent!")
            Log.addMesage("mail-module", "Email sent!")
        except Exception as ex:
            print("Something went wrong….", ex)
            Log.addMesage("mail-module", "Something went wrong…" + str(ex))

    def isNotEmpty():
        return len(body)