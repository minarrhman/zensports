# Generated by Django 2.2 on 2021-08-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210809_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, upload_to='videos/%Y/%m')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]