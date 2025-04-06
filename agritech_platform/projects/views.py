from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import render
from .models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projects/project_detail.html', {'project': project})
