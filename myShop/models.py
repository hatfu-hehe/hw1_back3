from django.db import models

class Category(models.Model):
    name_categ = models.CharField(max_length=100)

    def __str__(self):
        return self.name_categ

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter the name of the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.name} - {self.category.name_categ}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
