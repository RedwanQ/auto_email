from email import message
from http import server
import smtplib
import ssl
from email.message import EmailMessage


subject = "Email From Python"
body = "This is a test email from Python"
sender = "virus.run.py@gmail.com"
receiver = "virus.run.py@gmail.com"
password = input("Enter password: ")

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject


html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending.....")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())

print("Succes!")