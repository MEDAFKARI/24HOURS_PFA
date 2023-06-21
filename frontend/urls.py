from django.urls import path, include
from .views import Home, Article_Details,Category,search
from .views import profile, unsave_article, createArticle,update, delete, DelCom
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home,name='Home'),
    path('',include('news.urls')),
    path('<int:id>/',Article_Details, name='article_detail'),
    path('Category/<slug:st>/', Category, name='Category'),
    path('search', search, name='search'),
    path('Rel/', include('users.urls')),
    path('profile/', profile, name='profile'), 
    path('profile/unsave/<int:id>/', unsave_article, name='unsave_article'),
    path('ArticleCreation', createArticle, name='Create'),
    path('Update/<int:id>/', update, name='Update'),
    path('CommentDelete/<int:id>/', DelCom, name='DelCom'), 
    path('Delete/<int:id>/', delete, name='delete'), 
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)