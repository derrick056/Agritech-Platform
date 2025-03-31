from django.urls import path
from .views import RegisterView  # Import the RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
