# Generated by Django 5.1.6 on 2025-03-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_students_gender_alter_students_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photo',
            field=models.CharField(max_length=255, verbose_name='Фото'),
        ),
    ]
