from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
     path('', views.product_list, name='product_list'),
     path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
     path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
     path('oplata.html', views.product_detail,
         name='product_oplata'),
     path('login', views.LoginView.as_view(), name='login'),
     path('logout', views.LogoutView.as_view(), name='logout'),
     path('signup', views.signup_view, name='signup'),
]