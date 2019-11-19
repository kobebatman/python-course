import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Python Course'
email['to'] = 'pythonehlelclass@gmail.com'
email['subject'] = 'Email using Python'

email.set_content('HELLO')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pythonehlelclass@gmail.com', 'password123#$')
    smtp.send_message(email)
    print('sent email!')