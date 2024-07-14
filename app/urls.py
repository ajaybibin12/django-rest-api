from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('products/', views.get_products, name='products'),  # Define a URL pattern for '/products/'
    path('/api/sigup/',views.user_signup,name="user_signup"),
]
