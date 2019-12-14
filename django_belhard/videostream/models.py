from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
# Create your models here.

class MyVideo(models.Model):
    title = models.CharField(max_length=100, default='NameLess', verbose_name='название', help_text='Название видео')
    slug = models.SlugField(max_length=50, unique=True, help_text='уникальная ссылка') #для уникальных имен
    description = models.TextField(blank=True, null=True)#для пустого поля! null=True обязательно!!!!
    likes = models.PositiveIntegerField(default=0, verbose_name='лайки')
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self): #магический метод вызывается каждый раз, когда выводит на печеть объект
        return f"{self.title} - {self.slug[:10]}"

    @property
    def player(self): #маленький плеер в админке
        return mark_safe(f"<iframe width='200' height='150' src='{self.url}'></iframe>") #Пометить как безопасно


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    video = models.ForeignKey(MyVideo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)