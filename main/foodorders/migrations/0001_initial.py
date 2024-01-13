# Generated by Django 4.2.7 on 2024-01-08 13:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublicId', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Quantity', models.IntegerField(default=1)),
                ('Specification', models.CharField(default=None, max_length=200)),
                ('Status', models.BooleanField(default=True)),
                ('MenuItem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.menu')),
            ],
            options={
                'db_table': 'main.foodOrders',
            },
        ),
    ]