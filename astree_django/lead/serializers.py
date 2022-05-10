from .models import Lead
from rest_framework import serializers


class LeadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lead
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'assigned_to',
            'created_at',
            'modified_at',
        )