# Generated by Django 3.0.6 on 2020-06-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='view',
            field=models.CharField(default='table', max_length=5),
        ),
    ]