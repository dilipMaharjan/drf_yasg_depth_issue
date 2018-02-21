from rest_framework import viewsets

from todo.models import A, C, Chu, Co, P, T
from todo.serializer import ASerializer, CSerializer, ChuSerializer, CoSerializer, PSerializer, TSerializer, \
    TfSerializer


class AViewSet(viewsets.ModelViewSet):
    queryset = A.objects.all()
    serializer_class = ASerializer


class CViewSet(viewsets.ModelViewSet):
    queryset = C.objects.all()
    serializer_class = CSerializer


class ChuViewSet(viewsets.ModelViewSet):
    queryset = Chu.objects.all()
    serializer_class = ChuSerializer


class CoViewSet(viewsets.ModelViewSet):
    queryset = Co.objects.all()
    serializer_class = CoSerializer


class PViewSet(viewsets.ModelViewSet):
    queryset = P.objects.all()
    serializer_class = PSerializer


class TViewSet(viewsets.ModelViewSet):
    queryset = T.objects.all()
    serializer_class = TSerializer


class TfViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = T.objects.all()
    serializer_class = TfSerializer
