from django.contrib.auth.models import User,Group
from rest_framework import viewsets,permissions
from .serializers import GroupSerializer,UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    api end point that allows user to viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow to group update and viewed.
    """
    queryset = Group.objects.all()
    serializer_class = Group
    permission_classes = [permissions.IsAuthenticated]
