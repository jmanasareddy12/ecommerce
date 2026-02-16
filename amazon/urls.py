from django.urls import path
from . import views

urlpatterns=[
    path('',views.product_list,name='product_list'),
    path('product/<int:id>/',views.product_details,name='product_details'),
    path('add/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/<int:id>/',views.view_cart,name='view_cart'),
]