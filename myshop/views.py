from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .models import Category, Product, User
from cart.forms import CartAddProductForm
from .forms import *
from django.views.generic import View

from django.db.models import Q


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        products = Product.objects.filter(name__icontains=q) 
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                      {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form' : cart_product_form})

def about(request):
    return render(request, 'product/about.html')

class LoginView(View):
    form_class = LoginForm
    template_name = 'users/login_page.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('shop:product_list'))
            else:
                HttpResponse('Invalid account')
        return render(request, self.template_name, {'form': form})
    

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('shop:product_list'))


def search_view(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        products = Product.objects.filter(Q(name__contains=searched))
        print(searched)
        print(products)
        return render(request, 'shop/search.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'shop/search.html')