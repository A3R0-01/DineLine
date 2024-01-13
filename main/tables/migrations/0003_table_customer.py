# Generated by Django 4.2.7 on 2024-01-02 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_customers', '0001_initial'),
        ('tables', '0002_table_funcstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main_customers.customer', unique=True),
        ),
    ]
