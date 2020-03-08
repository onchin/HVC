from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Branch(models.Model):
    branchID = models.IntegerField(blank=False, null=False, primary_key=True)
    branchCity = models.CharField(max_length=50, default=None)


class Address(models.Model):
    addressID = models.IntegerField(blank=False, null=False, primary_key=True)
    street1 = models.CharField(max_length=50, default=None)
    street2 = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=2, default=None)
    zipcode = models.IntegerField(blank=True, null=True)


class Comment(models.Model):
    commentID = models.IntegerField(blank=False, null=False, primary_key=True)
    comment = models.CharField(max_length=150, default=None)
    author = models.CharField(User, max_length=250, blank=False, null=False)


class Account(models.Model):
    choice = [(1, 'Active'), (2, 'Inactive')]
    accountNumber = models.IntegerField(blank=False, null=False, primary_key=True)
    status = models.BooleanField(choices=choice, default=1, blank=False)
    accountType = models.CharField(max_length=50, default=None)
    balance = models.FloatField(null=False, blank=False)


class Customer(models.Model):
    customerID = models.IntegerField(blank=False, null=False, primary_key=True)
    firstName = models.CharField(max_length=50, default=None)
    lastName = models.CharField(max_length=50, default=None)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, blank=False, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=None, blank=False, null=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None, blank=False, null=False)










