from rest_framework import viewsets
from .models import User, Category, Product, ShoppingCart, CartItem, Review, Wishlist, WishlistItem
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer,CategorySerializer, ProductSerializer, ShoppingCartSerializer, CartItemSerializer, ReviewSerializer, WishlistSerializer, WishlistItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User created successfully!",
                    "user": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(username=username)

                # Check if the password matches the hashed password
                if check_password(password, user.password):
                    # Generate JWT token if the password is correct
                    refresh = RefreshToken.for_user(user)
                    response = Response({
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    }, status=status.HTTP_200_OK)

                    return response
                else:
                    return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetailView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')

        try:
            user = self.get_queryset().get(pk=user_id)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        serializer = self.get_serializer(user)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def list(self, request, *args, **kwargs):
        category_id = self.request.query_params.get('category', None)
        cache_key = "products_list_all" 
        print(request.user)
        products = self.get_queryset().select_related('category')
        if category_id:
            try:
                products = products.filter(category_id=category_id)
                if not products.exists():
                    return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

                cache_key = f"products_list_of_{category_id}" 
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        
        serializer = self.get_serializer(products, many=True)
        cache.set(cache_key, serializer.data, timeout=60 * 5)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        cache_key = f'product_detail_{product_id}'
        cached_product = cache.get(cache_key)
        if cached_product:
            return Response(cached_product)

        try:
            product = self.get_queryset().select_related('category').get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        

        serializer = self.get_serializer(product)
        cache.set(cache_key, serializer.data, timeout=60 * 5)  
        return Response(serializer.data)


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class WishlistItemViewSet(viewsets.ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer


