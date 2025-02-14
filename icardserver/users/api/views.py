from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from users.models import User

class UserApiPViewSet(ModelViewSet):
  permission_class=[IsAdminUser]
  #serializer_class=UserS
  queryset=User.objects.all()