# Generated by Django 2.2 on 2021-08-09 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_intro_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intro',
            name='name',
        ),
    ]
