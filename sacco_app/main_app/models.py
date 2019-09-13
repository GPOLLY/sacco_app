from __future__ import unicode_literals
from django.db import models


# maintaniance menu
# general paramter
class General_paramter(models.Model):
	general_code = models.CharField(max_length = 10, blank = True , null= True, unique=True)
	general_name = models.CharField(max_length = 100, blank = True , null= True)

	def __unicode__ (self):
		return self.general_par

# banksetup
class Bank_setup(models.Model):
	bank_code = models.CharField(max_length = 10, blank = True , null= True, unique=True)
	bank_name = models.CharField(max_length = 100, blank = True , null= True)

	def  __unicode__(self):
	 	return self.bank 

# production defination
class Products_defination(models.Model):
	prod_code = models.CharField(max_length = 10, blank = True , null= True)
	pname = models.CharField(max_length = 100, blank = True , null= True)
	prefix = models.CharField(max_length = 10, blank = True , null= True)
	pro_category = models.CharField(max_length = 80, blank = True , null= True, unique=True)
	pro_period = models.IntegerField(default=0)

	def __unicode__(self):
		return self.products
# relationship code
class Relationship(models.Model):
	relation_code =models.CharField(max_length =10, blank = True, null =True)
	relation_name = models.CharField(max_length = 100, blank = True, null = True)

	def __unicode__(self):
		return relation
#accounts setup
class Accounts_setup(models.Model):
	account_number = models.CharField(max_length = 18, blank = False, null = False) 
	account_name = models.CharField(max_length = 255, blank = False, null = False)
	def __unicode__(self):
		return account
# annual budget
class Budget_setup(models.Model):
	account_number = models.CharField(max_length = 18, blank = False, null = False) 
	account_name = models.CharField(max_length = 255, blank = False, null = False)
	account_budget = models.FloatField(default = 0)
	def __unicode__(self):
		return budget

# purpose of a loan
class Loan_purpose(models.Model):
	purpose_code = models.CharField(max_length =10, blank=True, null = True)
	purpose_name = models.CharField(max_length = 100, blank = True,null =True)
	def __unicode__(self):
		return loan



