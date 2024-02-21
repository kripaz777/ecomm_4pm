from .views import *
from django.urls import path,include

urlpatterns = [
    path("",HomeView.as_view(),name = "home"),
    path("category/<slug>", CategoryView.as_view(), name="category"),
    path("brand/<slug>", BrandView.as_view(), name="brand"),
    path("signup", signup, name="signup"),
    path("add_to_cart/<slug>", add_to_cart, name="add_to_cart"),
    path("my_cart",CartView.as_view(),name = "my_cart"),
]