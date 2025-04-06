

from django.db import models
from projects.models import Project

class Investment(models.Model):
    project = models.ForeignKey(Project, related_name='investments', on_delete=models.CASCADE)
    investor_name = models.CharField(max_length=100)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    invested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor_name} invested in {self.project.title}"
