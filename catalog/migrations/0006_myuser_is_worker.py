# Generated by Django 3.1 on 2020-09-15 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200831_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_worker',
            field=models.BooleanField(default=False),
        ),
    ]
