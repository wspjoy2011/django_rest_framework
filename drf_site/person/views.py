from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict

from .models import Person, Category
from .serializers import PersonSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class PersonAPIList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PersonAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PersonAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': {cat.id: cat.name for cat in cats}})

# class PersonAPIList(generics.ListCreateAPIView):
#     """
#     Post and get requests
#     """
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
#
# class PersonAPIUpdate(generics.UpdateAPIView):
#     """
#     Put request
#     """
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
#
# class PersonAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     All CRUD operations
#     """
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


# class PersonAPIView(APIView):
#     def get(self, request):
#         persons = Person.objects.all()
#         return Response({'posts': PersonSerializer(persons, many=True).data})
#
#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if pk is None:
#             return Response({"error": 'Method put is not allowed'})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = PersonSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if pk is None:
#             return Response({'error': 'Method DELETE is not allowed'})
#         try:
#             Person.objects.get(pk=pk).delete()
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         return Response({"post": f"delete post - {pk}"})

# class PersonAPIView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
