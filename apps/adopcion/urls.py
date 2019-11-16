
from django.conf.urls import url
from apps.adopcion.views import idx_adopcion

urlpatterns = [
    url(r'^index$', idx_adopcion),
]