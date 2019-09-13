from django import forms
from .models import *

# general paramter
class GeneralparamterForm(forms.ModelForm):
	general_code = forms.CharField()
	general_name = forms.CharField()

	class Meta:
		model = General_paramter
		fields =["general_code",
		"general_name",
		]
# banksetup
class BanksetForm(forms.ModelForm):
	bank_code = forms.CharField()
	bank_name = forms.CharField()
	class Meta:
		model =Bank_setup
		fields =["bank_code",
		"bank_name",
		]

# product defination
class ProductForm(forms.ModelForm):
	prod_code = forms.CharField()
	pname = forms.CharField()
	prefix = forms.CharField()
	pro_category = forms.CharField()
	pro_period = forms.IntegerField()

	class Meta:
		model = Products_defination
		fields=["prod_code",
		"pname",
		"prefix",
		"pro_category",
		"pro_period",]

# relationform
class RelationForm(forms.ModelForm):
	relation_code = forms.CharField()
	relation_name = forms.CharField()
	class Meta:
		model = Relationship
		fields =["relation_code",
		"relation_name",]

#accountsform
class AccountsForm(forms.ModelForm):
	account_number = forms.CharField()
	account_name = forms.CharField()
	class Meta:
		model = Accounts_setup
		fields = ["account_number",
		"account_name",] 

#budget
class BudgetForm(forms.ModelForm):
	account_number = forms.CharField()
	account_name = forms.CharField()
	account_budget = forms.FloatField()

	class Meta:
		model = Budget_setup
		fields =["account_number",
		"account_name",
		"account_budget",]

# purposeform
class PurposeloanForm(forms.ModelForm):
	purpose_code = forms.CharField()
	purpose_name = forms.CharField()
	class Meta:
		fields=["purpose_code",
		"purpose_name",]

