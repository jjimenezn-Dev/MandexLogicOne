from django.urls import path
from . import views

urlpatterns = [
    path('', views.deliver_list, name='deliver_list'),
    path('<int:deliver_id>/', views.deliver_detail, name='deliver_detail'),
]
