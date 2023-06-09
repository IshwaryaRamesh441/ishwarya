# Generated by Django 4.1.6 on 2023-05-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'foodmenu',
                'verbose_name_plural': 'foodmenus',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='breakfast',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
