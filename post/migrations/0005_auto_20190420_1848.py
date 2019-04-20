# Generated by Django 2.2 on 2019-04-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False),
        ),
    ]
