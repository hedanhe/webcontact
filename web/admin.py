from django.contrib import admin

# Register your models here.
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','hidden','publish_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','article','user','comment','parent_comment')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','user')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
admin.site.register(models.ThumbUp)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.UserGroup)