# Generated by Django 2.2 on 2019-04-20 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descriptoin',
            new_name='description',
        ),
    ]
