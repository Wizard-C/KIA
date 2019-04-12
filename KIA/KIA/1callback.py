import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtpObj.starttls())
print('Login')
login=smtpObj.login('wizardc391@gmail.com','piyb0714')
print('Mail')
smtpObj.sendmail("wizardc391@gmail.com","Blue   SkyC@mail.ru","go to bed!")
print('End')
smtpObj.quit()
