import imp
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


from .models import Lead
from .serializers import LeadSerializer
# Create your views here.
class LeadPagination(PageNumberPagination):
    page_size = 2

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)