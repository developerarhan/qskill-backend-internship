from django.urls import path

from .views import CustomTokenObtainPairView, RegiserView


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegiserView.as_view(), name="register"),
]