from django.shortcuts import render

# Create your views here.
from rest_framework import views, response
from .serializers import InvestmentSerializer

class InvestmentCreateView(views.APIView):
    def post(self, request):
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Investment recorded successfully'})
        return response.Response(serializer.errors, status=400)
