from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    # TokenVerifyView,
)

app_name = 'api'

urlpatterns = [
    # path("", views.get_routes, name='home'),
    path("notes", views.notes_api, name='notes'),
    path("notes/<int:pk>", views.note_api, name='note'),
    path("create/", views.create, name='create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]