from django.contrib import admin
from .models import Author
from .article_model import Article 


admin.site.register(Article)
admin.site.register(Author)
