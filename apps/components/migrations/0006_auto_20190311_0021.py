# Generated by Django 2.1.5 on 2019-03-11 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_auto_20190310_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamme',
            name='nature',
        ),
        migrations.RemoveField(
            model_name='module',
            name='price',
        ),
        migrations.AddField(
            model_name='gamme',
            name='quality',
            field=models.CharField(choices=[('EXL', 'excellence'), ('LUX', 'luxe'), ('NAT', 'natural')], default='NAT', max_length=3, verbose_name='quality'),
        ),
        migrations.AddField(
            model_name='module',
            name='angle',
            field=models.IntegerField(null=True, verbose_name='angle'),
        ),
        migrations.AddField(
            model_name='module',
            name='length2',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='length'),
        ),
    ]
