# Generated by Django 2.1.5 on 2019-03-31 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190311_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maderauser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/users-media/avatars/'),
        ),
    ]
