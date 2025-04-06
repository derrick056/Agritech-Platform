from rest_framework import viewsets, permissions
from .models import Investment
from .serializers import InvestmentSerializer
from django.shortcuts import render

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all().order_by('-invested_at')
    serializer_class = InvestmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(investor=self.request.user)

def investment_list(request):
    investments = Investment.objects.all()
    return render(request, 'investment/investment_list.html', {'investments': investments})

def investment_detail(request, id):
    investment = Investment.objects.get(id=id)
    return render(request, 'investment/investment_detail.html', {'investment': investment})

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer