from django.db import models

class Groups(models.Model):
    name = models.CharField('Наименование', max_length=50)
    course = models.IntegerField('Курс')
    speciality = models.ForeignKey('Specialities', on_delete=models.CASCADE)
    count_of_students = models.IntegerField('Количество студентов', default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Specialities(models.Model):
    name = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'