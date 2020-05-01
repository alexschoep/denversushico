# Import smtplib for the actual sending function
import smtplib

class EmailMessage():
  def __init__(self, reservation):
    self.sender = 'alexschoep1@gmail.com'
    self.recipient = reservation.email
    self.subject = f'Your Reservation for Denver Sushi Company'
    self.body = f'Hello {reservation.name}.\n\nYou have reserved a table at Denver Sushi Company for {reservation.date} at {reservation.time}\nTo edit your reservation, please visit 127.0.0.1:8000/reserve/{reservation.url}'

  def send(self):
    s = smtplib.SMTP()
    s.connect('email-smtp.us-west-2.amazonaws.com', 587)
    s.starttls()
    s.login('AKIATZJK7MLN63BJP3XL', 'BILJJ8pcDa1sBMwVLBapWXg1qNtdQvL+YONGJVWjghEA')
    msg = f'From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n\n{self.body}'
    s.sendmail(self.sender, self.recipient, msg)