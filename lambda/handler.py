import sys
sys.path.insert(0, 'package/')
from config import EMAIL_ADDRESS, \
                   EMAIL_PASS, \
                   SENDGRID_API_KEY
import smtplib
from email.message import EmailMessage
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def send_email(subject, content, to_):
    """Send email

    Args:
        subject(str): subject of email
        content(str): content of email
        to_(str): email to receive
    """
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = EMAIL_ADDRESS
    message['To'] = to_
    message.set_content(content)
    print(message)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
            smtp.send_message(message)
            logger.info("send_email: Message sent to email: %s" % (to_))
    except Exception as err:
        logging.error("send_email: Message not sent to %s"
                      % (to_))
        raise Exception(err)


def send_email_sendgrid(subject, content, to_):
    """Send email

    Args:
        subject(str): subject of email
        content(str): content of email
        to_(str): email to receive
    """
    message = Mail(
        from_email='daniel.pereiracosta@hotmail.com',
        to_emails=to_,
        subject=subject,
        # html_content='<strong>and easy to do anywhere, even with Python</strong>'
        plain_text_content=content)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        logger.info("send_email: Message sent to email: %s" % (to_))
    except Exception as e:
        logging.error("send_email: Message not sent to %s"
                      % (to_))
        logging.error(e.body)
        raise Exception(e)


def lambda_handler(event, context):
    for message in event['data']:
        subject = message['subject']
        content = message['message']
        to_ = message['to']
        # send_email(subject, content, to_)
        send_email_sendgrid(subject, content, to_)


if __name__ == '__main__':
    event = {
        'data': [{
        'subject': 'HELLO THERE!',
        'message': 'NICE MEETING YOY',
        'to': 'TEST_EMAIL@gmail.com'
    }]}
    lambda_handler(event, None)
