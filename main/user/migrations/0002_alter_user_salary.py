# Generated by Django 4.2.7 on 2023-12-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Salary',
            field=models.IntegerField(),
        ),
    ]
