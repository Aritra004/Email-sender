from email.message import EmailMessage
import ssl
import smtplib

email_sender='aritradebnath9@gmail.com'
email_password='ouifjhtuyectwvjy'

email_reciever='legipi5132@mirtox.com'

subject="Dont forget to drink coffee"
body="""
When you are coding drink coffee
"""

em=EmailMessage()
em['From']=email_sender
em['to']=email_reciever
em['subject']=subject
em.set_content(body)


context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())

