from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()
    views['contacts'] = ContactInfo.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        try:
            username = request.user.username
            self.views['count_cart'] = Cart.objects.filter(username=username, checkout=False).count()
        except:
            pass
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['products'] = Product.objects.all()
        self.views['hots'] = Product.objects.filter(label = 'hot')
        self.views['news'] = Product.objects.filter(label = 'new')
        self.views['sales'] = Product.objects.filter(label = 'sale')
        return render(request,'index.html',self.views)


class CategoryView(BaseView):
    def get(self,request,slug):
        self.views
        try:
            username = request.user.username
            self.views['count_cart'] = Cart.objects.filter(username=username, checkout=False).count()
        except:
            pass
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_product'] = Product.objects.filter(category_id = cat_id)
        return render(request,'category.html',self.views)


class BrandView(BaseView):
    def get(self,request,slug):
        self.views
        try:
            username = request.user.username
            self.views['count_cart'] = Cart.objects.filter(username=username, checkout=False).count()
        except:
            pass
        b_id = Brand.objects.get(slug = slug).id
        self.views['brand_product'] = Product.objects.filter(brand_id = b_id)
        return render(request,'brand.html',self.views)

class SearchView(BaseView):
    def get(self,request):
        if request.method == 'GET':
            query = request.GET['query']
            if query != "":
                self.views['search_product'] = Product.objects.filter(name__icontains = query)
        return render(request,'search.html',self.views)
def signup(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already exists!")
                return redirect('/sighup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already in use!")
                return redirect('/sighup')
            else:
                User.objects.create_user(
                    first_name = fname,
                    last_name = lname,
                    username = username,
                    email = email,
                    password = password
                ).save()
        else:
            messages.error(request, "Password does not match!")
            return redirect('/signup')
    return render(request,'signup.html')

def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(username = username, slug = slug,checkout = False).exists():
        quantity = Cart.objects.get(username=username, slug=slug, checkout=False).quantity
        quantity = quantity + 1
        price = Product.objects.get(slug = slug).price
        discounted_price = Product.objects.get(slug = slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
            total = original_price * quantity
        else:
            original_price = price
            total = original_price * quantity

        Cart.objects.filter(username=username, slug=slug, checkout=False).update(
            quantity = quantity,
            total = total
        )
    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        Cart.objects.create(
            username = username,
            slug = slug,
            total = original_price,
            item = Product.objects.filter(slug = slug)[0]
        ).save()
    return redirect('/my_cart')

def reduce_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(username = username, slug = slug,checkout = False).exists():
        quantity = Cart.objects.get(username=username, slug=slug, checkout=False).quantity
        if quantity > 1:
            quantity = quantity - 1
            price = Product.objects.get(slug = slug).price
            discounted_price = Product.objects.get(slug = slug).discounted_price
            if discounted_price > 0:
                original_price = discounted_price
                total = original_price * quantity
            else:
                original_price = price
                total = original_price * quantity

            Cart.objects.filter(username=username, slug=slug, checkout=False).update(
                quantity = quantity,
                total = total
            )
    return redirect('/my_cart')

def delete_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(username=username, slug=slug, checkout=False).exists():
        Cart.objects.filter(username=username, slug=slug, checkout=False).delete()

    return redirect('/my_cart')
class CartView(BaseView):
    def get(self,request):
        try:
            username = request.user.username
            self.views['count_cart'] = Cart.objects.filter(username=username, checkout=False).count()
        except:
            pass
        carts = Cart.objects.filter(username = username,checkout = False)
        self.views['cart_product'] = carts
        all_total = 0
        for i in carts:
            all_total = all_total + i.total
        self.views['all_total'] = all_total
        # self.views['delivery'] = 50
        self.views['grand_total'] = all_total + 50
        return render(request,'cart.html',self.views)
