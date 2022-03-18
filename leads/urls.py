from django.urls import path
from .views import lead_detail, lead_list

# app_name = "leads"

urlpatterns = [
    path('', lead_list, name="lead_list"),
    path('<int:pk>/', lead_detail, name="lead_detail")
]