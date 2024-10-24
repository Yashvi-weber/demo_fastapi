import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender, receiver, subject, body):

    # SMTP Configuration (for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "yashvisavajgdgssasit@gmail.com"
    smtp_pass = "dpffibhcvjlztpay"

    #build the mail system to send someone
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    #now try to send the mail to receiver 

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


import random

otp = random.randint(1000, 9999)

# Email details
send_email("yashvisavajgdgssasit@gmail.com", #sender
           "yashvisavaj2121@gmail.com",#reciver
             "Test Email", f"Otp is {otp}")