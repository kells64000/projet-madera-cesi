# Generated by Django 2.1.5 on 2019-02-03 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190203_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maderauser',
            name='username',
        ),
    ]