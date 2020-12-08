from apps.comments.views import CommentsView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', CommentsView)
urlpatterns = router.urls