# Generated by Django 2.2.6 on 2020-01-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200102_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchecksingleton',
            name='highest_block_checked',
            field=models.CharField(default='6889000', max_length=78),
        ),
    ]