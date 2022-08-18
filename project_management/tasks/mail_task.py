import os
import smtplib
import ssl


def send_email(receiver_email, planned_type):
    port = 587
    smtp_server = os.environ.get('SMTP_SERVER', "smtp.gmail.com")
    sender_email = os.environ.get('SENDER_EMAIL', "EXAMPLEproject_management@gmail.com")
    receiver_email = receiver_email
    password = os.environ.get('SENDER_PASSWORD', "EXAMPLEproject_managementPassword")
    message = """\
        Subject: Project Time Problem

        Work has passed the planned {planned_type} date""".format(planned_type=planned_type)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
