from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    '''帖子表'''
    title = models. CharField(u"文章标题",max_length=255, unique=True)
    category = models.ForeignKey('Category',verbose_name=u"帖子板块", on_delete=models.CASCADE)
    head_img = models.ImageField(upload_to="uploads")
    summary = models.CharField(u"总结", max_length=225)
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile", verbose_name=u"作者",on_delete=models.CASCADE)
    publish_date = models.DateTimeField(u"日期", auto_now=True)
    hidden = models.BooleanField(u'是否隐藏', default=True)
    priority = models.IntegerField(u"优先级",default=1000)

    def __str__(self):
        return "%s, author:%s" %(self.title, self.author)


class Comment(models.Model):
    '''评论表'''
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    #blank=True是django.admin可以为空;null=True是数据库可以为空
    parent_comment = models.ForeignKey('self', related_name='p_comment',blank=True, null=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s, user:%s" %(self.comment, self.user)

class ThumbUp(models.Model):
    '''点赞'''
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "user:%s" %(self.user)

class Category(models.Model):
    '''帖子板块'''
    name = models.CharField(max_length=64,unique=True)
    admin = models.ManyToManyField('UserProfile')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    '''用户信息'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGroup', blank=True, null=True)
    #symmetrical=默认对称
    friends = models.ManyToManyField('self', blank=True, related_name='my_friend')


    def __str__(self):
        return self.name

class UserGroup(models.Model):
    '''用户组'''
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name