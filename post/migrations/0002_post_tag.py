# Generated by Django 2.2 on 2019-04-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='post.Tag', verbose_name='Теги'),
        ),
    ]
