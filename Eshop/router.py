from Eshop.viewsets import UserViewsets, CategoryViewsets, ProductViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewsets)
# router.register(r'order', views.OrderViewSet)
router.register(r'category', CategoryViewsets)
router.register(r'product', ProductViewsets)