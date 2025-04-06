from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class Investment(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='investments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    invested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.investor.username} invested in {self.project.title}'
