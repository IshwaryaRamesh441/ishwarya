# Generated by Django 4.1.6 on 2023-05-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_chatitems_combooffer_dailyspecial_freshjuice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='bimage',
            field=models.ImageField(upload_to=''),
        ),
    ]
