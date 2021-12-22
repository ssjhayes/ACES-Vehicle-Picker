from django.db import models
from django.db.models.fields.related import ForeignKey

# Set up the models for dependent dropdown for vehicle selection
class Make(models.Model):
	name = models.CharField(max_length=50)

class Model(models.Model):
	name = models.CharField(max_length=50)
	make = models.ForeignKey(Make, on_delete=models.CASCADE)

class Submodel(models.Model):
	name = models.CharField(max_length=50)
	model = models.ForeignKey(Model, on_delete=models.CASCADE)

class Year(models.Model):
	year = models.IntegerField()
	submodel = models.ManyToManyField(Submodel)

# Model for housing complete vehicle information
class Vehicle(models.Model):
	make = models.ForeignKey(Make, on_delete=models.CASCADE)
	model = models.ForeignKey(Model, on_delete=models.CASCADE)
	submodel = models.ForeignKey(Submodel, on_delete=models.CASCADE)
	year = models.ForeignKey(Year, on_delete=models.CASCADE)

	def __str__(self):
		return (self.year.year + ' ' + self.make.name + ' ' + self.model.name + ' ' + self.submodel.name)
