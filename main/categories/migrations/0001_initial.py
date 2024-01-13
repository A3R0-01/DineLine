# Generated by Django 4.2.7 on 2024-01-03 09:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublicId', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.CharField(max_length=30)),
                ('FuncStatus', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'main.categories',
            },
        ),
    ]
