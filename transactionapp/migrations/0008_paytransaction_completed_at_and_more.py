# Generated by Django 4.2.8 on 2023-12-15 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactionapp', '0007_remove_paytransaction_completed_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytransaction',
            name='completed_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paytransaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
