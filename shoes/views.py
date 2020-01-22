from .models import Shoes
from .serializers import ShoesSerializer
from rest_framework import generics
from .permissions import IsAuthorReadOnly


# Create your views here.
class ShoesList(generics.ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

class ShoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
    permission_classes = (IsAuthorReadOnly, )