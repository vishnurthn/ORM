# Generated by Django 5.1.4 on 2024-12-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BankLoan",
            fields=[
                ("loan_id", models.IntegerField(primary_key=True, serialize=False)),
                ("loan_type", models.CharField(max_length=100)),
                ("loan_amt", models.FloatField()),
                ("cust_acno", models.IntegerField()),
                ("cust_name", models.CharField(max_length=50)),
            ],
        ),
    ]