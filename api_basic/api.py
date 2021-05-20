# from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
#from rest_framework import generics
#from rest_framework import mixins


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
