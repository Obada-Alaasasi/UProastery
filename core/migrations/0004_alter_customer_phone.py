# Generated by Django 4.1.6 on 2023-03-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_assign_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Customer',
            name='phone',
            field=models.IntegerField(null = False),
        ),
    ]