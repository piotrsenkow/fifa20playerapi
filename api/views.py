from rest_framework import generics
from .models import Gk, Cam, Cb, Cdm, Cf, Cm, Lb, Lm, Lw, Lwb, Rb, Rm, Rw, Rwb, St
from .serializers import GkSerializer, CamSerializer, CbSerializer, CdmSerializer, CfSerializer, CmSerializer, LbSerializer, LmSerializer, LwSerializer, LwbSerializer, RbSerializer, RmSerializer, RwSerializer, RwbSerializer, StSerializer
from api.paginations import StandardPagination
# Create your views here.


class GkRetrieveView(generics.RetrieveAPIView):

    queryset = Gk.objects.all()
    serializer_class = GkSerializer
    lookup_field = 'sofifa_id'


class CamRetrieveView(generics.RetrieveAPIView):

    queryset = Cam.objects.all()
    serializer_class = CamSerializer
    lookup_field = 'sofifa_id'


class CbRetrieveView(generics.RetrieveAPIView):
    queryset = Cb.objects.all()
    serializer_class = CbSerializer
    lookup_field = 'sofifa_id'


class CdmRetrieveView(generics.RetrieveAPIView):
    queryset = Cdm.objects.all()
    serializer_class = CdmSerializer
    lookup_field = 'sofifa_id'


class CfRetrieveView(generics.RetrieveAPIView):
    queryset = Cf.objects.all()
    serializer_class = CfSerializer
    lookup_field = 'sofifa_id'


class CmRetrieveView(generics.RetrieveAPIView):
    queryset = Cm.objects.all()
    serializer_class = CmSerializer
    lookup_field = 'sofifa_id'


class LbRetrieveView(generics.RetrieveAPIView):
    queryset = Lb.objects.all()
    serializer_class = LbSerializer
    lookup_field = 'sofifa_id'


class LmRetrieveView(generics.RetrieveAPIView):
    queryset = Lm.objects.all()
    serializer_class = LmSerializer
    lookup_field = 'sofifa_id'


class LwRetrieveView(generics.RetrieveAPIView):
    queryset = Lw.objects.all()
    serializer_class = LwSerializer
    lookup_field = 'sofifa_id'


class LwbRetrieveView(generics.RetrieveAPIView):
    queryset = Lwb.objects.all()
    serializer_class = LwbSerializer
    lookup_field = 'sofifa_id'


class RbRetrieveView(generics.RetrieveAPIView):
    queryset = Rb.objects.all()
    serializer_class = RbSerializer
    lookup_field = 'sofifa_id'


class RmRetrieveView(generics.RetrieveAPIView):
    queryset = Rm.objects.all()
    serializer_class = RmSerializer
    lookup_field = 'sofifa_id'


class RwRetrieveView(generics.RetrieveAPIView):
    queryset = Rw.objects.all()
    serializer_class = RwSerializer
    lookup_field = 'sofifa_id'


class RwbRetrieveView(generics.RetrieveAPIView):
    queryset = Rwb.objects.all()
    serializer_class = RwbSerializer
    lookup_field = 'sofifa_id'


class StRetrieveView(generics.RetrieveAPIView):
    queryset = St.objects.all()
    serializer_class = StSerializer
    lookup_field = 'sofifa_id'