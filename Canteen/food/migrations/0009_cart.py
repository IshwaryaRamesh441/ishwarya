# Generated by Django 4.1.6 on 2023-05-04 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_alter_chatitems_cimage_alter_combooffer_cimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast_qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('breakfast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.breakfast')),
            ],
        ),
    ]
