from news.models import categories

def All_cates(request):
    All_cates = categories.objects.all()
    return {'All_cates': All_cates}
