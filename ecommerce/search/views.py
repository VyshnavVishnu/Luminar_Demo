from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shop.models import Product


@login_required
def search_products(request):
    p = None
    query = ""
    if (request.method=="POST"):
        query = request.POST['search']
        if query:
            p = Product.objects.filter(p_name__icontains=query)
    return render(request,'search_products.html',{'query':query,'p':p})