from django.shortcuts import render
from django.views import View


class BaseView(View):
    views = {}


class HomeView(BaseView):
    def get(self,request):

        return render(request,'index.html')