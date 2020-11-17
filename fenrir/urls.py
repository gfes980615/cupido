from django.urls import path
from . import views
from . import get_latlng
from . import ig

urlpatterns = [
    path('', views.home),
    path('test', get_latlng.searchLatLng),
    path('ig', ig.get_ig)
]