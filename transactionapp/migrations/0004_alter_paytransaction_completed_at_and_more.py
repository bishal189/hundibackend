# Generated by Django 4.2.8 on 2023-12-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactionapp', '0003_auto_20231215_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytransaction',
            name='completed_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transfertransaction',
            name='completed_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]