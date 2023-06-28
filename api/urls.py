from django.urls import path
from rest_framework import routers
from .api import ProductViewSet
from .views import ProductView

router = routers.DefaultRouter()
router.register('add', ProductViewSet, 'api'),
path('', ProductView.as_view(), name='api'),

urlpatterns = router.urls