from django.shortcuts import render

def product(request):
    return render(request, 'product/product.html')

def product_detail(request, pk):
    return render(request, 'product/product_detail.html')