from rest_framework.routers import DefaultRouter
from .views import DataSetViewSet, DataRecordViewSet

router = DefaultRouter()
router.register(r'datasets', DataSetViewSet)
router.register(r'records', DataRecordViewSet)

urlpatterns = router.urls
