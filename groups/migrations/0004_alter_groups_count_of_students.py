# Generated by Django 5.1.6 on 2025-03-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_groups_count_of_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='count_of_students',
            field=models.IntegerField(verbose_name='Количество студентов'),
        ),
    ]
