# Generated by Django 2.2.2 on 2019-06-15 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 15, 19, 58, 7, 251882), verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entity',
            field=models.IntegerField(),
        ),
    ]
