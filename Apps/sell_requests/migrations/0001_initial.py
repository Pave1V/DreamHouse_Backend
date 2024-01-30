# Generated by Django 5.0.1 on 2024-01-16 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(db_index=True, default='address', max_length=100, verbose_name='Address')),
                ('sqft', models.CharField(db_index=True, default='SQFT', max_length=20, verbose_name='SQFT')),
                ('age_building', models.IntegerField(db_index=True, verbose_name='Age Building')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]