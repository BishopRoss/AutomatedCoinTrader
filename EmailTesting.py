import smtplib
import ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "bishoprossrossdevelopment@gmail.com"
receiver_email = "bishopross@gmail.com"
password = "Cyclops_64"
context = ssl.create_default_context()


def sendEmailAlert(coin, price):
    message2 = """\
Subject: COIN PRICE ALERT

{coin}'s price is at {price} and may be going down, watch it."""

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message2.format(coin=coin, price=price))

