from django.contrib import admin

from .models import Products, UserProfile, ImgProduct, Category, BufBasket, ListOrders, Coments, NoUserListOrders

admin.site.register(Products)
admin.site.register(ImgProduct)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(BufBasket)
admin.site.register(ListOrders)
admin.site.register(Coments)
admin.site.register(NoUserListOrders)

# Register your models here.
