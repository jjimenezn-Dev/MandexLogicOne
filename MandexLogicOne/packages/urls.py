from django.urls import path
from . import views

urlpatterns = [
    path('', views.package_list, name='package_list'),
    # Otras URLs según sea necesario
]
