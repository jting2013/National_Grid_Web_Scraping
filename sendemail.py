import smtplib
from config import *

def send_mail(amount,date,util_type,website):
    s = smtplib.SMTP('smtp.live.com',587)
    s.ehlo()
    s.starttls()
    s.login(Email_From, Email_PW_From)
    subject = 'Subject: 135 Utilities Bill\n\n'
    description = 'Amount is {0} for {1} and due on {2}\n\n{3}'.format(amount,util_type,date,website)
    s.sendmail(Email_From, Email_To, subject+description)
