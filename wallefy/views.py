from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CategorySerializer, InComeSerializer, OutComeSerializer
from .models import Category, InCome, OutCome


class CategoriesView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class InComesView(ListCreateAPIView):
    serializer_class = InComeSerializer
    queryset = InCome.objects.all()


class InComeView(RetrieveUpdateDestroyAPIView):
    serializer_class = InComeSerializer
    queryset = InCome.objects.all()


class OutComesView(ListCreateAPIView):
    serializer_class = OutComeSerializer
    queryset = OutCome.objects.all()


class OutComeView(RetrieveUpdateDestroyAPIView):
    serializer_class = OutComeSerializer
    queryset = OutCome.objects.all()
