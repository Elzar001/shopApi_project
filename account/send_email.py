from django.core.mail import send_mail


def send_confirmation_email(user):
    code = user.activation_code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    to_email = user.email
    send_mail('Здравствуйте, активируйте Ваш аккаунт!',
              f'Чтобы активировать Ваш аккаунт'f'нужно перейти по ссылке: {full_link}',
              'example@gmail.com', [to_email],
              fail_silently=False)


def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail('Восстановление пароля', f'Ваш код: {code}', 'from@example.com', [to_email],
              fail_silently=False)


def send_notification(user, id):
    to_email = user.email
    send_mail('Уведомление о создании заказа!!',
              f'Вы создали заказ №{id}. Ожидайте звонка от курьера, Спасибо за доверие',
              'market.place@gmail.com', [to_email], fail_silently=False)
