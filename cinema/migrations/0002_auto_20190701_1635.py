# Generated by Django 2.2.1 on 2019-07-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciname',
            name='names',
            field=models.CharField(max_length=256, verbose_name='影院名称'),
        ),
    ]
