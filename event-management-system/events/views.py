from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.exceptions import ValidationError

from .serializers import EventSerializer, RegistrationSerializer
from .models import Event, Registration
from .permissions import IsOrganizer, IsPlatform_Manager, IsEventOwner

# Create your views here.

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        queryset = Event.objects.all()

        user = self.request.user

        # Public users see only approved events
        if not user.is_authenticated :
            queryset = queryset.filter(is_approved=True)

        elif user.role == 'platform_manager':
            queryset = queryset
        
        elif user.role == 'organizer':
            queryset = queryset.filter(created_by=user)
        
        else:
            queryset = queryset.filter(is_approved=True)

        # Filters
        date = self.request.query_params.get('date')
        location = self.request.query_params.get('location')

        if date:
            queryset = queryset.filter(date__date=date)
        
        if location:
            queryset = queryset.filter(location__icontains=location)
        
        return queryset
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        
        # if self.action == 'register':
        #     return [IsAuthenticated()]
        
        if self.action == 'approve':
            return [IsAuthenticated(), IsPlatform_Manager()]

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOrganizer(), IsEventOwner()]
        
        return super().get_permissions()
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        event = self.get_object()
        event.is_approved = True
        event.is_rejected = False
        event.save()

        return Response (
            {"message": "Event approved successfully"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()

        serializer = RegistrationSerializer(
            data={'event': event.id},
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"message": "Registered successfully"}, status=201)
    
    @action(
        detail=False, methods=['get'], url_path='admin/pending', permission_classes=[IsAuthenticated, IsPlatform_Manager]
    )
    def pending(self, request):
        events = Event.objects.filter(is_approved=False)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
    
    @action(
    detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsPlatform_Manager]
    )
    def reject(self, request, pk=None):
        event = self.get_object()
        event.is_approved = False
        event.is_rejected = True
        event.save()

        return Response(
            {"message": "Event rejected successfully"},
            status=status.HTTP_200_OK
        )
    


class RegistrationViewSet(ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user, registered_at=now())
    
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')

    def get_queryset(self):
        # User can see only their registration
        return Registration.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['delete'])
    def cancel(self, request, pk=None):
        registration = self.get_object()
        registration.status = 'cancelled'
        registration.save()

        return Response(
            {"message": "Registration cancelled successfully"},
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['get'])
    def my(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    @action(
    detail=False, methods=['get'], url_path='admin', permission_classes=[IsAuthenticated, IsPlatform_Manager]
    )
    def admin_list(self, request):
        registrations = Registration.objects.all()
        serializer = self.get_serializer(registrations, many=True)
        return Response(serializer.data)
