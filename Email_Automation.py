import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail credentials
gmail_user = 'your_email@gmail.com'
gmail_password = 'your_password'

# Email details
subject = "Your Subject Here"
body = """
Hi,

This is a sample email body.

Best regards,
Your Name
"""

# List of recipients
recipients = [
    'recipient1@example.com',
    'recipient2@example.com',
    # Add more recipients here
]

# Function to send email
def send_email(to_email):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(gmail_user, to_email, text)
        server.quit()
        print(f'Email sent to {to_email}')
    except Exception as e:
        print(f'Failed to send email to {to_email}: {str(e)}')

# Send email to each recipient
for recipient in recipients:
    send_email(recipient)
