from django.contrib import admin
from .models import Customer, Account, Address, Branch, Comment

# Register your models here.


class CustomerList(admin.ModelAdmin):
    list_display = ('customerID', 'firstName', 'lastName', 'address', 'account', 'comment')
    list_filter = ('customerID', 'firstName', 'lastName', 'account')
    search_fields = ('customerID', 'firstName', 'lastName', 'account')
    ordering = ['customerID']


class BranchList(admin.ModelAdmin):
    list_display = ('branchID', 'branchCity')
    list_filter = ('branchID', 'branchCity')
    search_fields = ('branchID', 'branchCity')
    ordering = ['branchID']


class AddressList(admin.ModelAdmin):
    list_display = ('street1', 'street2', 'city', 'state', 'zipcode')
    list_filter = ('city', 'state', 'zipcode')
    search_fields = ('street1', 'street2', 'city', 'state', 'zipcode')
    ordering = ('state', 'city')


class AccountList(admin.ModelAdmin):
    list_display = ('accountNumber', 'status', 'accountType', 'balance')
    list_filter = ('accountNumber', 'status', 'accountType')
    search_fields = ('accountNumber', 'status', 'accountType')
    ordering = ('accountNumber',)


class CommentList(admin.ModelAdmin):
    list_display = ('commentID', 'comment', 'author')
    list_filter = ('commentID', 'author')
    search_fields = ('commentID', 'author')
    ordering = ('commentID',)


admin.site.register(Customer, CustomerList)
admin.site.register(Branch, BranchList)
admin.site.register(Address, AddressList)
admin.site.register(Account, AccountList)
admin.site.register(Comment, CommentList)


