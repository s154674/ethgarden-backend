# Generated by Django 2.2.6 on 2020-01-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_blockheight'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockCheckSingleton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_block_checked', models.CharField(max_length=78)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
