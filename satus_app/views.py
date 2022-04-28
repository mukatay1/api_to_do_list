from rest_framework import filters

from .permissions import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import ListPagination
from .serializers import *


class CurrentList(generics.ListCreateAPIView):
    permission_classes = [IsCreaterOrReadOnly]
    serializer_class = CurrentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    pagination_class = ListPagination

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

    def get_queryset(self):
        return Current.objects.filter(author=self.request.user.pk).order_by('-start')


class CurrentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCreaterOrReadOnly]
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer


class UserProfileView(APIView):
    permission_classes = [IsCreaterOrReadOnly]

    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            new_serializer = serializer.save(commit=False)
            new_serializer.user = profile.user.pk
            new_serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        profile = UserProfile.objects.get(pk=pk)
        user = User.objects.get(username=request.user)
        profile.delete()
        user.delete()
        return Response(status=status.HTTP_200_OK)


class ListView(generics.ListCreateAPIView):
    permission_classes = [IsCreaterOrReadOnly]
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    pagination_class = ListPagination


class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCreaterOrReadOnly]
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def perform_update(self, serializer):
        pk = self.kwargs['pk']
        flist = List.objects.get(pk=pk)
        serializer.save(author=flist.author)
