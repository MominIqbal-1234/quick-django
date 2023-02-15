

from django.urls import path
from app import views

urlpatterns = [
      path('',views.Home.as_view(),name=''),
]
        