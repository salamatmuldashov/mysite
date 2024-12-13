from rest_framework.routers import DefaultRouter
from .views import  RegisterView, LoginView ,UserDetailView,CategoryViewSet, ProductViewSet, ShoppingCartViewSet, CartItemViewSet, ReviewViewSet, WishlistViewSet, WishlistItemViewSet
from django.urls import path, include

router = DefaultRouter()


router.register(r'users', UserDetailView)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'shopping-carts', ShoppingCartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'wishlist-items', WishlistItemViewSet)


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls
