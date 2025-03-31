from django.shortcuts import render

# Create your views here.
from rest_framework import views, response
from .serializers import ProjectSerializer

class ProjectCreateView(views.APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Project created successfully'})
        return response.Response(serializer.errors, status=400)
