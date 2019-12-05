# Generated by Django 2.2.6 on 2019-12-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grownevent',
            name='grown_by',
        ),
        migrations.AddField(
            model_name='grownevent',
            name='block_number',
            field=models.CharField(default='', max_length=78),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grownevent',
            name='transaction_hash',
            field=models.CharField(default='', max_length=66),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transferevent',
            name='transaction_hash',
            field=models.CharField(default='', max_length=66),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grownevent',
            name='plant_id',
            field=models.CharField(max_length=78),
        ),
        migrations.AlterField(
            model_name='grownevent',
            name='seed',
            field=models.CharField(max_length=78),
        ),
        migrations.AlterField(
            model_name='transferevent',
            name='block_number',
            field=models.CharField(max_length=78),
        ),
        migrations.AlterField(
            model_name='transferevent',
            name='plant_id',
            field=models.CharField(max_length=78),
        ),
        migrations.AddIndex(
            model_name='grownevent',
            index=models.Index(fields=['block_number'], name='events_grow_block_n_44c544_idx'),
        ),
        migrations.AddIndex(
            model_name='grownevent',
            index=models.Index(fields=['transaction_hash'], name='events_grow_transac_52ecd3_idx'),
        ),
        migrations.AddIndex(
            model_name='grownevent',
            index=models.Index(fields=['plant_id'], name='events_grow_plant_i_7deabf_idx'),
        ),
        migrations.AddIndex(
            model_name='transferevent',
            index=models.Index(fields=['block_number'], name='events_tran_block_n_2e1234_idx'),
        ),
        migrations.AddIndex(
            model_name='transferevent',
            index=models.Index(fields=['transaction_hash'], name='events_tran_transac_86a512_idx'),
        ),
        migrations.AddIndex(
            model_name='transferevent',
            index=models.Index(fields=['plant_id'], name='events_tran_plant_i_e705d7_idx'),
        ),
        migrations.AddIndex(
            model_name='transferevent',
            index=models.Index(fields=['from_address'], name='events_tran_from_ad_a61977_idx'),
        ),
        migrations.AddIndex(
            model_name='transferevent',
            index=models.Index(fields=['to_address'], name='events_tran_to_addr_1320b2_idx'),
        ),
    ]
