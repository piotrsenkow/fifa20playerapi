from rest_framework import generics
from .models import Gk
from .serializers import GkSerializer
from api.paginations import StandardPagination
# Create your views here.


class GkRetrieveView(generics.RetrieveAPIView):

    queryset = Gk.objects.all()
    serializer_class = GkSerializer
    lookup_field = 'sofifa_id'
