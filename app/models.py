from django.db import models

def upl(instance,fileName):
    return f"products/{instance.name}/{fileName}"

class Product(models.Model):
    name = models.CharField(max_length=100,unique=True)
    info = models.TextField(blank=True,null=True)
    price = models.PositiveIntegerField(blank=False,null=False)
    image = models.ImageField(upload_to=upl,blank=False,null=False)
    discount = models.PositiveSmallIntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.name}"