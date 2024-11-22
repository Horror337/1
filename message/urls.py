from .views import messageView , aboutView
from django.urls import path



urlpatterns = [
    path('',messageView.as_view(),name="home"),
    path('about/', aboutView.as_view(),name='about'),
]
