from django.db import models

class YandexMemberModel(models.Model):
    name = models.TextField("Имя и фамилия",default='')
    phone = models.TextField("Номер телефона",default='')
    login = models.TextField("Логин",default='')
    password = models.TextField("Пароль",default='')
    proxy_string = models.TextField("Прокси строка",default='')
    last_time = models.DateTimeField("Дата и время последнего обновления онлайна")


    def __str__(self):
        return f"{self.name}, {self.phone}"


    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'