# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendEmail(reservation):
  #disable
  print('disable')
  return False
  print('enable')
  message = Mail(
      from_email='no-reply@denversushicompany.com',
      to_emails=reservation.email,
      subject='Your Reservation at Denver Sushi Company',
      html_content=f"<p>Hello {reservation.name}</p><p>You have created a reservation for {reservation.time} on {reservation.date}</p><p>To edit or delete your reservation, go to <a href='denversushicompany.com/reserve/{reservation.url}/edit'>this link</a>.<p>")
  try:
      sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except Exception as e:
      print(e.message)