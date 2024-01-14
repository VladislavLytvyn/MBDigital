from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from api.serializers import PersonSerializer, GroupSerializer
from api.models import Person, Group


class PersonList(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission = IsAuthenticated

    def perform_create(self, serializer):
        serializer.save()


class PersonDetail(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission = IsAuthenticated


class GroupList(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission = IsAuthenticated

    def perform_create(self, serializer):
        serializer.save()


class GroupDetail(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission = IsAuthenticated
