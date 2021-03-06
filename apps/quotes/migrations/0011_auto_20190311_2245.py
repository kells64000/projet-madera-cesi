# Generated by Django 2.1.5 on 2019-03-11 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0010_auto_20190310_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='client',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client', to='users.Client'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='salesperson',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesperson', to='users.SalesPerson'),
        ),
    ]
