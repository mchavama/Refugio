
from django.conf.urls import url, include
from apps.mascota.views import index

urlpatterns = [
   url(r'^index$', index),
]
