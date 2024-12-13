from django.contrib import admin

from .models import User, Category, Product, ShoppingCart, CartItem, Review, Wishlist, WishlistItem

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
