# Generated by Django 4.1.6 on 2023-02-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='opis',
            field=models.TextField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='img',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
