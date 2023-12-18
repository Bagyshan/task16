from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_human),
    path('get/', get_humans),
    path('get/<int:pk>/', get_humans),
    path('update/<int:pk>/', update_human),
    path('delete/<int:pk>/', delete_human)
]