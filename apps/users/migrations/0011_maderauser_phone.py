# Generated by Django 2.1.5 on 2019-03-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_client_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='maderauser',
            name='phone',
            field=models.CharField(blank=True, max_length=12, verbose_name='phone'),
        ),
    ]
