# Generated by Django 2.0.1 on 2018-02-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_user', '0003_auto_20180127_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='sheng',
            field=models.CharField(default='', max_length=8),
        ),
    ]