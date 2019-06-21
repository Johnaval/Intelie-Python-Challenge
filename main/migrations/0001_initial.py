# Generated by Django 2.2.2 on 2019-06-15 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=200)),
                ('attribute', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 6, 15, 17, 57, 50, 939343), verbose_name='modified')),
                ('validation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=200, unique=True)),
                ('cardinality', models.CharField(choices=[('one', 'one'), ('many', 'many')], default='one', max_length=4)),
            ],
        ),
    ]