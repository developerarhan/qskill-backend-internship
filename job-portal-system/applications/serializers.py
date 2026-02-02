from rest_framework import serializers

from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields =  [
            'id',
            'job',
            'applicant_name',
            'email',
            'phone',
            'resume',
            'cover_letter',
            'applied_at'
        ]
        read_only_fields = ['user', 'applied_at']