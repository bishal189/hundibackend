# Generated by Django 4.2.8 on 2023-12-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactionapp', '0008_paytransaction_completed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='paytransaction',
            name='Amount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='transfertransaction',
            name='receivedAmount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='transfertransaction',
            name='sentAmount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
