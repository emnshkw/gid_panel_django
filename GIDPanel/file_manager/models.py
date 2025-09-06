# downloads/models.py
from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f'ID - {self.id}, {self.name}'


    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = 'Файлы'


