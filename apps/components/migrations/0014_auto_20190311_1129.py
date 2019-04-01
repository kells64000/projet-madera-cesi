# Generated by Django 2.1.5 on 2019-03-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0013_auto_20190311_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='gamme',
            new_name='gammes',
        ),
        migrations.AlterField(
            model_name='gamme',
            name='ratio',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='ratio'),
        ),
    ]