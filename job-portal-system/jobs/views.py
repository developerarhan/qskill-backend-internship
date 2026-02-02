from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Job
from .serializers import JobSerializer
from .permissions import IsRecruiter
# Create your views here.

class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        queryset = Job.objects.all()

        allowed_filters = ['title', 'location', 'company']
        job_dict = {}

        for key, value in self.request.query_params.items():
            if key in allowed_filters:
                job_dict[key + "__icontains"] = value

        if job_dict:
            queryset = Job.objects.filter(**job_dict)

        # Recruiters only see their own jobs
        if self.request.user.is_authenticated and self.request.user.role == 'recruiter':
            queryset = queryset.filter(created_by=self.request.user)
        
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsRecruiter()]
        
        return super().get_permissions()     
    
    def destroy(self, request, *args, **kwargs):
        job = self.get_object()
        self.perform_destroy(job)
        return Response(
            {"message": "Job deleted successfully"},
            status=status.HTTP_200_OK
        )