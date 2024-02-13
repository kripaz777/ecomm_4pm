from django.shortcuts import render
from django.views import View
from .models import *

class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()
    views['contacts'] = ContactInfo.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['products'] = Product.objects.all()
        self.views['hots'] = Product.objects.filter(label = 'hot')
        self.views['news'] = Product.objects.filter(label = 'new')
        self.views['sales'] = Product.objects.filter(label = 'sale')
        return render(request,'index.html',self.views)