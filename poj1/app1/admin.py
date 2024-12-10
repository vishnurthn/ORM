from django.contrib import admin
from .models import BankLoan , BankLoanAdmin
# Register your models here.
admin.site.register(BankLoan , BankLoanAdmin)