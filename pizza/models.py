from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse

# Create your models here.
class PizzaVault(models.Model):
	Choices = [('regular','Regular'),('square','Square')]
	options = [('small','Small'),('medium','Medium'),('large','Large'),('exra-large','Extra-Large'),('massive','Massive')]
	top = [('pepperoni','Pepperoni'),('mushroom','Mushrooms'),('onions','Onions'),('sausage','Sausage'),('bacon','Bacon'),('extra cheese','Extra cheese'),('black olives','Black olives'),('tomato','Tomato'),('capsicum','Capsicum')]
	types = models.CharField(max_length=10, choices=Choices, default='regular')
	size = models.CharField(max_length=10, choices=options, default=None)
	toppings = MultiSelectField(choices=top,default=None, max_choices=3)

	def __str__(self): 
		return self.types


