from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import Product, Clothes, PC, Productasperhtml

# Create your views here.
def product_view(request):
    context = Productasperhtml.objects.all()
    return render(request, 'products.html',{'title':'Product Page - Admin HTML Template', 'products':'active', 'context': context})

def add_product(request):
    if request.method == 'POST':
        # Accessing form data
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        image = request.FILES.get('image')  # Access the uplaoded image
        stock = request.POST.get('stock')
        price = request.POST.get('price')
        
        # Map category value to a readable string
        category_map = {
            '1': 'new arrival',
            '2': 'most popular',
            '3': 'trending',
        }
        category = category_map.get(category, 'unknown')
        
        # Create and save the product
        Productasperhtml.objects.create(
            name= name,
            des=description,
            category= category,
            stock = stock,
            price = price,
            image= image,   # Save the uploaded file
            )
        
        # Redirect to the success page
        return redirect ('products')
    return render(request, 'add-product.html',{'title':'Add Product - Dashboard HTML Template', 'products':'active'})

def edit_product(request):
    return render(request, 'edit-product.html', {'title':'Edit Product - Dashboard Admin Template', 'products':'active'})

def add_product_form(request):
    return HttpResponse("This is Add Product page using the form from django")


def edit_product_form(request):
    return HttpResponse("This is Edit Product page using the form from django")
    pass

def filter_product(request):
    
    return HttpResponse("This is Filter Product page using the form from django")
    pass

def edit_product_specific(request, product_id):
    product = get_object_or_404(Productasperhtml, id=product_id)
    if request.method == 'post':
        # Update the product fields
        product.name = request.POST.get('name')
        product.des = request.POST.get('description')
        # product.category = request.POST.get('category') Need to replace all the category values to id value of the category
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        
    context = {'product':product}
    return render(request, 'edit-product.html', context)

def product_api(request):
    products = Productasperhtml.objects.all()
    my_product_list = []
    for product in products:
        product_obj = {
            'name': product.name,
            'description': product.des,
            'category': product.category,
            'price': product.price,
            'updated price': product.updated_price,
            'stock': product.stock,
            'image': product.image.url,
                       }
        my_product_list.append(product_obj)
    
    return JsonResponse({'data': my_product_list})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {'product': product})