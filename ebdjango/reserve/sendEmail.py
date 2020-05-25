# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

def sendEmail(reservation):
  message = Mail(
      from_email='no-reply@denversushicompany.com',
      to_emails=reservation.email,
      subject='Your Reservation at Denver Sushi Company',
      html_content=f"<p>Hello {reservation.name},</p><p>You have created a reservation for {reservation.time.strftime('%I:%M %p')} on {reservation.date.strftime('%A, %b %w, %Y')}.</p><p>To edit or delete your reservation, go to <a href='denversushicompany.com/reserve/{reservation.url}/edit'>this link</a>.</p><p>*Please note that Denver Sushi Co is not a real restaurant. This site is a programming test project. More info at <a href=alexschoep.net>alexschoep.net</a>.</p>")
  try:
      sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except Exception as e:
      print(e.message)