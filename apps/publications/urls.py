from apps.publications.views import PublicationsView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', PublicationsView)
# router.register(r'tags/{pk}', PublicationsView, basename='tag')
urlpatterns = router.urls
