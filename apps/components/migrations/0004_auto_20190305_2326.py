# Generated by Django 2.1.5 on 2019-03-05 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0003_auto_20190227_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gamme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('nature', models.CharField(max_length=20, null=True, verbose_name='nature')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('nature', models.CharField(max_length=20, verbose_name='nature')),
                ('length', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='length')),
                ('width', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='width')),
                ('depth', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='depth')),
                ('unit', models.CharField(max_length=10, verbose_name='unit')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='price')),
            ],
        ),
        migrations.RemoveField(
            model_name='component',
            name='designer',
        ),
        migrations.AddField(
            model_name='component',
            name='family',
            field=models.CharField(choices=[('EX', 'exterior'), ('IN', 'insulator'), ('CV', 'cover')], max_length=3, null=True, verbose_name='family'),
        ),
        migrations.AlterField(
            model_name='component',
            name='nature',
            field=models.CharField(choices=[('SYN', 'synthetic'), ('NAT', 'natural'), ('BIO', 'biological')], max_length=3, verbose_name='nature'),
        ),
        migrations.AddField(
            model_name='module',
            name='component',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mod_component', to='components.Component'),
        ),
        migrations.AddField(
            model_name='module',
            name='designer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='designer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamme',
            name='module',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module', to='components.Module'),
        ),
    ]