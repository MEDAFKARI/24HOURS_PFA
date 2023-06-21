from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.title}" 


class articles(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    desc = models.TextField(null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)   
    def __str__(self):
        return f"{self.title}" 


class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(articles, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.article.title} (saved by {self.user.username})"
    


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(articles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user}" 



