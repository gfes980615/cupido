from django.urls import path
from . import views
from . import get_latlng

urlpatterns = [
    path('', views.home),
    path('test', get_latlng.searchLatLng),
]