from django.urls import path

from . import views


app_name = 'product'


urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path('create/', views.ProductCreate.as_view(), name='product-create'),
]