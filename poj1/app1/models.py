from django.db import models
from django.contrib import admin

# create your models here
class BankLoan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=100)
    loan_amt = models.FloatField()
    cust_acno = models.IntegerField()
    cust_name = models.CharField(max_length=50)

class BankLoanAdmin(admin.ModelAdmin):
    list_display=('loan_id','loan_type','loan_amt','cust_acno','cust_name')