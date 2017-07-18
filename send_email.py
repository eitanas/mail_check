import smtplib

SUBJECT = "test_email"
TEXT = 'testing'
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
##content = 'test_mail'

FROM = 'eitanas85@gmail.com'
TO = 'eitanas85@gmail.com'

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(FROM, 'ea5283040')

mail.sendmail(FROM, TO, message)