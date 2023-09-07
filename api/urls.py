from rest_framework.routers import DefaultRouter

from api.views import ContactViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
urlpatterns = router.urls
