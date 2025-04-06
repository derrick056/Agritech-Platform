from django.urls import path, include
from .views import project_list
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from . import views

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('view/', project_list, name='project-list-html'),
    path('details/<int:id>/', views.project_detail, name='project-detail'),
]
