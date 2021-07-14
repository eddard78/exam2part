from django.contrib import admin
from django.urls import path, include
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from users.views import UserView
from products.views import ProductView, ProductCategoryView
from orders.views import OrderView

router = routers.DefaultRouter()

router.register(r'users', UserView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', LoginView.as_view(), name = 'rest_login'),
    path('signup/', RegisterView.as_view(), name = 'rest_register'),
    path('products/', ProductView.as_view({'get': 'list'})),
    path('products/categories/', ProductCategoryView.as_view({'get': 'list'})),
    path('orders/', OrderView.as_view({'get': 'list', 'post': 'create'})),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls