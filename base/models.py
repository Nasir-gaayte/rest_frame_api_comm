from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name



class ProductsModel(models.Model):
    name =models.CharField(max_length=50)
    image = models.ImageField(blank=True,null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    price = models.CharField(max_length=10)
    desc = models.TextField(null=True,blank=True)
    post_date = models.DateField(auto_now_add=True)    
