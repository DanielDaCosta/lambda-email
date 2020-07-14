from os import getenv
# import boto3
from dotenv import load_dotenv
load_dotenv()


EMAIL_ADDRESS = getenv('EMAIL_ADDRESS')
EMAIL_PASS = getenv('EMAIL_PASS')
SENDGRID_API_KEY = getenv('SENDGRID_API_KEY')
