import smtplib

class Mail:
    def init():
        global mail_user, mail_password, sent_from, to, subject, body
        body = ""

        mail_user = 'pia.generic@gmail.com'
        mail_password = 'piageneric99'

        sent_from = mail_user
        to = ['iuliuantoniu@gmail.com']
        subject = 'Weather status update!'

    def addContent(content):
        global body
        body += content + "\n"

    def send():
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(mail_user, mail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….", ex)

    def isNotEmpty():
        return len(body)