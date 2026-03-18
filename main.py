from utils import send_email, load_emails

def main():
    sender = input("Enter your email: ")
    password = input("Enter your app password: ")

    choice = input("Send to (1) Single email or (2) Multiple emails? ")

    if choice == "1":
        receiver = input("Enter receiver email: ")
        receivers = [receiver]
    else:
        receivers = load_emails()

    subject = input("Subject: ")
    body = input("Message: ")

    file_path = input("Enter file path (or press Enter to skip): ")

    send_email(sender, password, receivers, subject, body, file_path)


if __name__ == "__main__":
    main()