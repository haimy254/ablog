# Generated by Django 4.0.4 on 2023-06-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='blog', max_length=255),
        ),
    ]
