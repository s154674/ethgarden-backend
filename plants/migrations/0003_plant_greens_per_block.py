# Generated by Django 2.2.6 on 2019-12-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20191205_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='greens_per_block',
            field=models.SmallIntegerField(default=10),
        ),
    ]
