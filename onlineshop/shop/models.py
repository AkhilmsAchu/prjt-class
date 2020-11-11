from django.db import models

# Create your models here.
class property(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	img = models.ImageField(upload_to='propertypic',default='demo.png')

	def __str__(self):
		return self.name
	 