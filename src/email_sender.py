import smtplib
from email.message import EmailMessage

def send_email(receiver_email):

    sender_email = "prabha08082006@gmail.com"
    app_password = "qhbqqzmhtdhqvzzl"

    msg = EmailMessage()

    msg["Subject"] = "Smart Resume Analyzer Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        "Hello,\n\nYour Smart Resume Analyzer Report is attached.\n\nThank you."
    )

    with open("resume_report.pdf", "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="Resume_Report.pdf"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("✅ Email Sent Successfully")