# Generated by Django 2.1.5 on 2019-01-27 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaderaUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='assets/users-media/avatars/')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('maderauser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                        parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_pro', models.BooleanField(default=False, verbose_name='is pro')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.maderauser',),
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SalesPerson',
            fields=[
                ('maderauser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                        parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('workplace', models.CharField(blank=True, max_length=20, verbose_name='workplace')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.maderauser',),
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='maderauser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                         related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='maderauser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set',
                                         related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]