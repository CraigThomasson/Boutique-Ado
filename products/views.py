from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ a veiw to show all producs and sorting and seaching """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)