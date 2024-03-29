# Generated by Django 5.0.1 on 2024-01-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_index=True, max_length=100, verbose_name='user name')),
                ('password', models.CharField(db_index=True, max_length=50, verbose_name='password')),
                ('email', models.EmailField(db_index=True, max_length=50, verbose_name='email')),
                ('token', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='token')),
                ('token_expires', models.DateTimeField(blank=True, null=True, verbose_name='Token expires date/time: ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date/time: ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date/time: ')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
