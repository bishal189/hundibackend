# Generated by Django 4.2.8 on 2023-12-15 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactionapp', '0005_alter_transfertransaction_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfertransaction',
            name='completed_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
