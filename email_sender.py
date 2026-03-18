import smtplib
from email.message import EmailMessage

def send_email():
    sender = input("Enter your email: ")
    password = input("Enter your app password: ")
    receiver = input("Enter receiver email: ")

    subject = input("Subject: ")
    body = input("Message: ")

    
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print(" Error:", e)


if __name__ == "__main__":
    send_email()