# Generated by Django 2.2.4 on 2019-09-05 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary_app', '0004_auto_20190905_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='bio',
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary_app.Entry')),
            ],
        ),
    ]
