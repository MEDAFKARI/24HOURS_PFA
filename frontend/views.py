from django.shortcuts import render
from news.models import articles, categories, SavedArticle, Comment
import requests
from django.shortcuts import redirect
from django.core.paginator import Paginator
from news.forms import articlesCreationForm, articlesUpdateForm
from datetime import datetime


# Create your views here.



def Home(request):
    data = articles.objects.all().order_by('-date')
    paginator = Paginator(data, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    is_first_page = page_obj.number == 1

    return render(request, 'home.html', {'page_obj': page_obj, 'is_first_page': is_first_page, 'data':data})



def Article_Details(request, id):

    art = articles.objects.get(id=id)
    saved_article = None
    is_saved = False

    if request.method == 'POST' and request.user.is_authenticated:
        if 'save_article_btn' in request.POST:
            saved_article = SavedArticle.objects.filter(user=request.user, article=art).first()
            if not saved_article:
                saved_article = SavedArticle(user=request.user, article=art)
                saved_article.save()

    if request.user.is_authenticated:
        saved_article = SavedArticle.objects.filter(user=request.user, article=art).first()
        if saved_article:
            is_saved = True

    if request.method == 'POST':
        content = request.POST.get('comment')
        if content:
            comment = Comment.objects.create(article =art, user=request.user, content=content)
            comment.save()

    comments = Comment.objects.filter(article=art)


    return render(request,
                  'Article.html',
                  {'art' : art,
                   'saved_article' : saved_article,
                   'comments':comments})


def Category(request, st):

    cat = categories.objects.get(title = st)
    data = articles.objects.all().filter(category = cat).order_by('-date')
    paginator = Paginator(data, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    return render(request, 'home.html', {'page_obj': page_obj})


from django.db.models import Q


def search(request):
    query = request.GET.get('q')
    
    results = articles.objects.filter(title__icontains=query) | articles.objects.filter(category__title__icontains=query)
    
    paginator = Paginator(results, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'search.html', {'query': query, 'page_obj': page_obj})



def profile(request):
    saved = SavedArticle.objects.filter(user=request.user)
    return render(request, 'profile.html', {'saved':saved})


def unsave_article(request, id):
    saved_article = SavedArticle.objects.get(id=id, user=request.user)
    saved_article.delete()
    return redirect('profile')


def createArticle(request):
    if request.method == 'POST':
        form = articlesCreationForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('Home')
    else:
        form = articlesCreationForm()

    return render(request, 'CreateArticle.html', {'form':form})


def update(request, id):
    article_to_update = articles.objects.get(id=id)
    form = articlesUpdateForm(instance=article_to_update)

    if request.method == "POST":
        form = articlesUpdateForm(request.POST, request.FILES, instance=article_to_update)
        if form.is_valid():
            form.save()
            return redirect('Home')

    context = {
        'form': form
    }
    return render(request, 'UpdateArti.html', context)



def delete(request,id):
    a_to_delete=articles.objects.get(id=id)
    a_to_delete.delete()

    return redirect('Home')



def DelCom(request,id):
    C=Comment.objects.get(id=id)
    article_id =C.article.id
    
    C.delete()
    return redirect('article_detail', id=article_id)





    