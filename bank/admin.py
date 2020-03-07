from django.contrib import admin
from .models import Customer, Account, Address, Branch

# Register your models here.


class CustomerList(admin.ModelAdmin):
    list_display = ('customerID', 'firstName', 'lastName')
    list_filter = ('customerID', 'firstName', 'lastName')
    search_fields = ('customerID', 'firstname', 'lastName')
    ordering = ['customerID']


class BranchList(admin.ModelAdmin):
    list_display = ('branchID', 'branchCity')
    list_filter = ('branchID', 'branchCity')
    search_fields = ('branchID', 'branchCity')
    ordering = ['branchID']


class AddressList(admin.ModelAdmin):
    list_display = ('street1', 'street2', 'city', 'state', 'zipcode', 'customerID')
    list_filter = ('city', 'state', 'zipcode', 'customerID')
    search_fields = ('street1', 'street2', 'city', 'state', 'zipcode', 'customerID')
    ordering = ('state', 'city')


class AccountList(admin.ModelAdmin):
    list_display = ('accountNumber', 'status', 'accountType', 'balance', 'customerID')
    list_filter = ('accountNumber', 'status', 'accountType', 'customerID')
    search_fields = ('accountNumber', 'status', 'accountType', 'customerID')
    ordering = ('accountNumber',)


admin.site.register(Customer, CustomerList)
admin.site.register(Branch, BranchList)
admin.site.register(Address, AddressList)
admin.site.register(Account, AccountList)



