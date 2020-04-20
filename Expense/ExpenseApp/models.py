from django.db import models

# Create your models here.

class Expenses(models.Model):

	Title = models.CharField(max_length=100, blank=False)
	Price = models.CharField(max_length=50)
	Capital = models.BooleanField(default=False)

   
	FYCHOICE = ( 
          ('2018','2018'),
		('2019/2020','2019/2020'),
		('2020/2021','2020/2021'),
		('2021/2022','2021/2022'),
		('2022/2023','2022/2023'),
		('2023/2024','2023/2024'),
		)
	Choices = ( 
     ('Work', 'Work'),
     ('Charity', 'Charity'),
     ('Tax', 'Tax'),
     ('Water', 'Water'),
     ('Council', 'Council'),
     ('Insurance', 'Insurance'),
     ('Land Tax', 'Land Tax'),
     ('Repairs', 'Repairs'),
     ('Sundry', 'Sundry'),
     ('Interest', 'Interest'),
     ('Garden', 'Garden'),
     ('Property Agent', 'Property Agent'),
     ('Borrowing', ' Borrowing'),
     ('Depreciation', 'Depreciation'),
     ('Pest', 'Pest'),
     ('Advertising', 'Advertising'),
     (' Stationary', 'Stationary'),
     ('Telephone', 'Telephone'),
     ('Postage', 'Postage'),
     (' Electicity', 'Electicity'),
     ('Gas', 'Gas'),
     ('Conveyancing', 'Conveyancing'),
     ('Meeting', 'Meeting'),
     ('Admin', 'Admin'),
     ('Fees', 'Fees'),
     ('Lawyer', 'Lawyer'),
     ('Marketing', 'Marketing'),
     ('Store', 'Store'),
     ('Brokage','Brokage'),
     ('Travel','Travel'),
     ('Bank Statement', 'Bank Statement'),
     )
	Date = models.CharField(max_length=15,blank=True)
	FY = models.CharField(max_length=50, choices=FYCHOICE,default="")
	Category = models.CharField(max_length=50, choices=Choices,default="")
	Image = models.FileField(blank=True)

     

class Farhan(Expenses):
	pass

class Nadia(Expenses):
	pass

class FarhanFamily(Expenses):
	pass

class Ongie(Expenses):
	pass

class Orange(Expenses):
	pass