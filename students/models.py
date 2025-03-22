from django.db import models
from groups.models import Groups

class Students(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Отчество', max_length=50, null=True, default='-')
    birthday = models.DateField('Дата рождения')
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    gender = models.ForeignKey('Genders', on_delete=models.CASCADE)
    is_leader = models.BooleanField('Староста или нет')
    photo = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.surname
    
    def get_absolute_url(self):
        return f'/students/{self.id}'
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Genders(models.Model):
    gender = models.CharField('Пол', max_length=10)

    def __str__(self):
        return self.gender
    
    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Полы'