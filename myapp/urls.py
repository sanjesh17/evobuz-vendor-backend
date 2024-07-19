from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.views.generic import RedirectView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', RedirectView.as_view(url='/api/', permanent=False)),  # Redirect root to API root
]