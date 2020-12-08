from apps.tags.views import TagView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TagView)
urlpatterns = router.urls