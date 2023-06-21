from django.contrib import admin
from news.models import articles,categories,SavedArticle,Comment

# Register your models here.

admin.site.register(articles)

admin.site.register(categories)


admin.site.register(SavedArticle)

admin.site.register(Comment)