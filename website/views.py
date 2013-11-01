# Create your views here.
from serializers import UserSerializer
from models import User
from django.http import HttpResponse

def UserList(request):
    users = User.objects.all()
    userSerial = UserSerializer(users, many=True)
    return HttpResponse(userSerial.data)