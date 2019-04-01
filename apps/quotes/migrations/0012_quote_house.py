# Generated by Django 2.1.5 on 2019-03-12 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0015_auto_20190311_1336'),
        ('quotes', '0011_auto_20190311_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='house',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='house', to='components.House'),
        ),
    ]