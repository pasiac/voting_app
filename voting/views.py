from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from voting.models import Option, Poll
from voting.serializers import OptionSerializer, PollSerializer


class OptionViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class PollViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Poll.objects.filter(active=True).all()
    serializer_class = PollSerializer
