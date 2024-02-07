from django.urls import path
from . import views

urlpatterns = [
    path('<int:address_id>/', views.address_detail, name='address_detail'),
    # Otras URLs según sea necesario
]
