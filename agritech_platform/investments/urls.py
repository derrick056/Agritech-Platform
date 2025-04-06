from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentViewSet
from . import views
router = DefaultRouter()
router.register(r'investments', InvestmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('view/', views.investment_list, name='investment-list'),
    path('details/<int:id>/', views.investment_detail, name='investment-detail'),
]
