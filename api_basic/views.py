from django.shortcuts import render
from .models import Article


def home(request):
    context = {

        'articles': Article.objects.all()
    }
    return render(request, 'api_basic/home.html', context)

# class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
# mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#    serializer_class = ArticleSerializer
#    queryset = Article.objects.all()

# class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,
# mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#    serializer_class = ArticleSerializer
#    queryset = Article.objects.all()

#    lookup_field = 'id'

#    def get(self,request, id=None):

#        if id:
#            return self.retrieve(request)
#        else:
#            return self.list(request)

#    def post(self,request):
#        return self.create(request)

#    def put(self,request,id=None):
#        return self.update(request,id)

#    def delete(self,request,id):
#        return self.destroy(request,id)
