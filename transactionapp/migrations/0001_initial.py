# Generated by Django 4.2.8 on 2023-12-11 01:45

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
                ('created_at', models.DateField(auto_now_add=True)),
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
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentAmount', models.IntegerField()),
                ('receivedAmount', models.IntegerField()),
                ('status', models.CharField(choices=[('RECEIVED', 'Received'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], max_length=15)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('completed_at', models.DateField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactionapp.receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactionapp.sender')),
            ],
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(max_length=200)),
                ('currencyCode', models.CharField(max_length=4)),
                ('bankAccountNumber', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('companyWorker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
