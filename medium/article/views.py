from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .article_model import Article
from .serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        #articlesx = Article.objects.select_related('author').get(author_id=3)
        #print(articlesx.author.name)
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})
      
    def post(self, request):
        article = request.data.get('article')

        serializer = ArticleSerializer(data=article)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article= get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved= serializer.save()
        return Response({"success": "Article '{}' updated sucessfully".format(article_saved.title)})
                         
    def delete(self, request, pk):

        article=get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id'{}' jas been deleted".format(pk)},status=204)
        

