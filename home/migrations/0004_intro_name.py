# Generated by Django 2.2 on 2021-08-09 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210807_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
