import smtplib
from email.message import EmailMessage

def load_emails():
    try:
        with open("emails.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(" emails.txt not found!")
        return []


def add_attachment(msg, file_path):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data,
                           maintype='application',
                           subtype='octet-stream',
                           filename=file_name)
    except Exception as e:
        print(" Attachment error:", e)


def send_email(sender, password, receivers, subject, body, file_path=None):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)
    msg['Subject'] = subject
    msg.set_content(body)

    if file_path:
        add_attachment(msg, file_path)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)

        print(" Email sent successfully!")

    except Exception as e:
        print(" Error sending email:", e)