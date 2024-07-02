from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name= 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('', views.home, name='home'),
    path('products/', views.products, name= 'products'),
    path('customers/<str:pk_test>', views.customer,name = 'customer'),
    path('create_order/', views.createOrder,name = 'create_order'),
    path('update_order/<str:pk>/', views.updateOrder,name = 'update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder,name = 'delete_order'),
    path('create_product/', views.createProduct,name = 'create_product'),
    path('create_customer/', views.createCustomer,name = 'creat_customer'),
    path('update_customer/<str:pk>/', views.updateCustomer,name = 'update_customer'),  
    path('update_product/<str:pk>/', views.updateProduct,name = 'update_product'),  
    path('delete_product/<str:pk>/', views.deleteProduct,name = 'delete_product'),
]
