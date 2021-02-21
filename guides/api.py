from rest_framework import viewsets,permissions
from .serializers import GuidesSerializer
from .models import guide

class GuidesViewAPI(viewsets.ModelViewSet):
    serializer_class = GuidesSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = guide.objects.all()