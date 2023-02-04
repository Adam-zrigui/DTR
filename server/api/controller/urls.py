from django.urls import path
from .views import RoomViews
urlpatterns = [
    path('', RoomViews.as_view())
]
