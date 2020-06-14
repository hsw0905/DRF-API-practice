from rest_framework.routers import SimpleRouter
from .views import CardViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', CardViewSet, basename='cards')
urlpatterns = router.urls