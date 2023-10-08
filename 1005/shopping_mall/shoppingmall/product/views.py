from django.shortcuts import render

def product(request):
    return render(request, 'product/product.html')

def pro_detail(request, pk):
    return render(request, 'product/pro_detail.html')