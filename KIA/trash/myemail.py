import smtplib

# Настройки
print('Записываю данные')
mail_sender = 'BlueSkyC@mail.com'
mail_receiver = 'wizardc391@gmail.ru'
username = 'BlueSkyC@mail.com'
password = '391731hOz'

# Формируем тело письма
print('Формирую письмо')
message = 'test_test_test <br>test'

# Отпавляем письмо
print('Подключаюсь к серверу')
session = smtplib.SMTP('smtp.mail.ru', 465)
print('Ввожу данные')
session.login(username, password)
print('Отправляю письмо')
session.sendmail(sender, mail_receiver, message)

# Как вариант рабочий код

# https://docs.google.com/document/d/1mqeUMUNVVgjbqCorfT40nAkkIn1bT9JryTYNMDqx5g8/edit
# Словарь кодера
