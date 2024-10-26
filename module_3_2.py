
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    flag = False
    com1 = recipient[len(recipient)-4:]
    ru1 = recipient[len(recipient)-3:]
    com2 = sender[len(sender)-4:]
    ru2 = sender[len(sender) - 3:]
    if "@" not in recipient or "@" not in sender:
        flag = True
    if ".com" != com1 and ".net" != com1 and ".ru" != ru1:
        flag = True
    if ".com" != com2 and ".net" != com2 and ".ru" != ru2:
        flag = True
    if flag:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
