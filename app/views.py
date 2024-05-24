from django.shortcuts import render
from .models import Product
def main(request):
    products = Product.objects.all()
    return render(request,"index.html",context={"data":products})