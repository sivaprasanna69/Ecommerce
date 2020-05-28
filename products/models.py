from django.db import models

# Create your models here.

class product(models.Model):

	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)


	def __str__(self):

		return self.title

	class Meta:
		unique_together = ('title', 'slug')
			

	def get_price(self):

		return self.price

class productImage(models.Model):
	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='product/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.product.title
		