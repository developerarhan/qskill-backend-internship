from django.db import transaction
from rest_framework import serializers
from rest_framework.response import Response

from .models import Event, Registration

class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    is_approved = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Registration
        fields = '__all__'
        read_only_fields = ['registered_at', 'status']

    def validate(self, data):
        user = self.context['request'].user
        event = data['event']

        # Event must be approved
        if not event.is_approved:
            raise serializers.ValidationError("This event is not approved yet.")
        
        if Registration.objects.filter(
            user=user, event=event, status='registered'
        ).exists():
            raise serializers.ValidationError(
                "You are already registered for this event."
            )
        
        return data
    
    def create(self, validated_data):
        user = self.context['request'].user
        event = validated_data['event']

        with transaction.atomic():
            event = Event.objects.select_for_update().get(pk=event.pk)

            if Registration.objects.filter(
                event=event, status='registered'
            ).count() >= event.capacity:
                raise serializers.ValidationError("Event is full.")
            
        return Registration.objects.create(
            user=user,
            event=event,
            status='registered'
        )