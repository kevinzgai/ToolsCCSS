# Generated by Django 2.2.1 on 2019-07-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_auto_20190701_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciname',
            name='cinemaCode',
            field=models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='影城编码'),
        ),
        migrations.AlterField(
            model_name='ciname',
            name='maoyanId',
            field=models.IntegerField(verbose_name='猫眼id'),
        ),
        migrations.AlterField(
            model_name='ciname',
            name='systemName',
            field=models.CharField(max_length=50, verbose_name='票务系统'),
        ),
        migrations.AlterField(
            model_name='ciname',
            name='taopiaopiaoId',
            field=models.IntegerField(verbose_name='淘票票id'),
        ),
    ]
