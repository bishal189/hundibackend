# Generated by Django 4.2.8 on 2023-12-15 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('bankName', models.CharField(max_length=100)),
                ('bankAccountNumber', models.CharField(max_length=100)),
                ('currencyCode', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('bankName', models.CharField(max_length=100)),
                ('currencyCode', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransferTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentAmount', models.FloatField()),
                ('receivedAmount', models.FloatField()),
                ('status', models.CharField(blank=True, choices=[('PROCESSING', 'Processing'), ('RECEIVED', 'Received'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactionapp.receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactionapp.sender')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumerName', models.CharField(max_length=100)),
                ('consumerId', models.CharField(blank=True, max_length=100, null=True)),
                ('companyName', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('Amount', models.FloatField()),
                ('status', models.CharField(blank=True, choices=[('PROCESSING', 'Processing'), ('RECEIVED', 'Received'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(max_length=200)),
                ('currencyCode', models.CharField(max_length=4)),
                ('bankAccountNumber', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('companyWorker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
