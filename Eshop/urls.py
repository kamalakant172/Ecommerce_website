from django.contrib import admin
from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.SignIn, name='sign_up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('cart', views.cart_info, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order', views.ord_info, name='order'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
