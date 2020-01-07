import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_html(data):
    html_text = ''
    for item in data:
        title = item['title']
        points = item['points']
        link = item['link']

        item_html = f'<li><a href="{link}">{title}</a>, <b>{points}</b></li>'
        html_text += item_html
    return f'''
    <html>
        <h3>Мэдээгээ хүлээн авна уу.</h3>
        <ol>
            {html_text}
        </ol>
    </html>'''

def send_email(data):
    msg = MIMEMultipart('alternative')
    msg['from'] = 'Сүүлийн үеийн мэдээ'
    msg['to'] = 'kobebatman92@gmail.com'
    msg['subject'] = 'Хамгийн их уншигдсан 10 мэдээ'

    html = MIMEText(get_html(data), 'html')
    msg.attach(html)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()

        smtp.login('python.angi2019@gmail.com', 'python2019')
        
        smtp.sendmail('python.angi2019@gmail.com', 'kobebatman92@gmail.com', msg.as_string())
        smtp.quit()