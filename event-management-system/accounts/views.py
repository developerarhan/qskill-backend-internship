from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serailizers import RegistrationSerializer

# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )

# Another way to write view for register using concrete generic view.

# class RegisterView(CreateAPIView):
# serializer_class = RegisterSerializer
# permission_classes = [AllowAny]

# def create(self, request, *args, **kwargs):
#     response = super().create(request, *args, **kwargs)
#     return Response(
#         {"message": "User registered successfully"},
#         status=status.HTTP_201_CREATED
#     )
