from django.contrib import admin
from .models import MyVideo, Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2
    readonly_fields = ['likes']


class MyVideoAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title', 'date', 'likes', 'player']
    #exclude = ['likes'] #отключает накрутку лайков
    readonly_fields = ['likes'] #Просто просмотр поля "без накрутки лайков"
    prepopulated_fields = {'slug': ['title']}


admin.site.register(MyVideo, MyVideoAdmin)