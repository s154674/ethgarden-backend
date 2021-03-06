# Generated by Django 2.2.6 on 2019-12-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('plant_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('owner', models.CharField(max_length=42)),
                ('last_green_calc', models.PositiveIntegerField()),
                ('plantTime', models.PositiveIntegerField()),
                ('seed', models.PositiveIntegerField(null=True)),
                ('value', models.PositiveIntegerField()),
                ('erc20_address', models.CharField(max_length=42)),
            ],
        ),
    ]
