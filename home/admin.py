from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Slider)
admin.site.register(Ad)
@admin.register(Product)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "price","category","label","brand","stock")
    ordering = ("id","name", "price","discounted_price")
    list_filter = ("category","label","brand","stock")
    search_fields = ("name","descripyion","specification" )

admin.site.register(Feedback)
admin.site.register(ContactInfo)
admin.site.register(Cart)
admin.site.register(ProductReview)
admin.site.register(Contact)