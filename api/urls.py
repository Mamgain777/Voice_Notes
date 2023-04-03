from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    # path("", views.get_routes, name='home'),
    path("notes", views.notes_api, name='notes'),
    path("notes/<int:pk>", views.note_api, name='note'),
]