from rest_framework.routers import DefaultRouter
from .views import CustomerInfoViewSet

router = DefaultRouter()
router.register(r'customerinfo', CustomerInfoViewSet)

urlpatterns = router.urls