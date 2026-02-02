from rest_framework import routers

from .views import EventViewSet, RegistrationViewSet

router = routers.SimpleRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'registrations', RegistrationViewSet, basename='registration')

urlpatterns = router.urls