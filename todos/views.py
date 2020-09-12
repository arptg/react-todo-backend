from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer, LabelSerializer, Todo, TodoLabel


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def update(self, request, *args, **kwargs):
        request.data['user'] = request.user_id
        return super().update(request, *args, **kwargs)


class TodoListCreateView (generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_id = self.request.user_id
        return Todo.objects.filter(user=user_id)

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user_id
        return super().create(request, *args, **kwargs)


class LabelListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LabelSerializer

    def get_queryset(self):
        user_id = self.request.user_id
        return TodoLabel.objects.filter(user=user_id)

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user_id
        return super().create(request, *args, **kwargs)
