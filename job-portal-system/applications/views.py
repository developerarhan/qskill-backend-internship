from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.

class ApplicationViewSet(ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show applications of logged-in user
        return Application.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='apply/(?P<job_id>[^/.]+)')
    def apply(self, request, job_id=None):
        # Copy the incoming JSON
        data = request.data.copy()  
        data['job'] = job_id

        serializer = ApplicationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user=request.user)
        except IntegrityError:
            return Response(
                {"error": "You have already applied for this job."},
                status=status.HTTP_400_BAD_REQUEST
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        job = self.get_object()
        self.perform_destroy(job)
        return Response(
            {"message": "Application deleted successfully."},
            status=status.HTTP_200_OK
        )