from django.db import models
 

class Book(models.Model):

	name = models.CharField(max_length=200)


class Parent(models.Model):
	parent_name = models.CharField(max_length=50)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=50)
	kid = models.ManyToManyField('Child', null=True, blank=True)

	def __str__(self):
		return self.parent_name

class Child(models.Model):
	child_name = models.CharField(max_length=100)
	dob = models.DateField()
	child_parent = models.ForeignKey('Parent', on_delete=models.CASCADE, verbose_name='Parent')

	def __str__(self):
		return self.child_name

