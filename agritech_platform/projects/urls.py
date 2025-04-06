from django.urls import path, include
from .views import project_list
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from . import views
from .views import project_list, project_with_investments

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('view/', project_list, name='project-list-html'),
    path('details/<int:id>/', views.project_detail, name='project-detail'),
    path('<int:project_id>/investments/', project_with_investments, name='project-with-investments'),
]
