# Generated by Django 2.2.4 on 2019-09-03 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary_app', '0009_auto_20190904_0220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='author',
            new_name='user',
        ),
    ]
