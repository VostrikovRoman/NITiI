# Generated by Django 5.1.6 on 2025-03-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_alter_students_lastname_alter_students_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
