from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from .forms import ArticleForm, handle_uploaded_file, CommentForm

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles':articles})

def category(request, category_id):

    articles = models.Article.objects.filter(category=category_id)
    return render(request, 'index.html', {'articles':articles})

def article_detail(request, category_id):
    try:
        article = models.Article.objects.get(id=category_id)
    except ObjectDoesNotExist as e:
        return render(request, '404.html', {'err_msg':u"您要查看的文章不存在"})
    return render(request, 'article.html', {'article_obj':article})

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def acc_login(request):
    err_msg = None
    if request.method == 'POST':

        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("ok")
            return HttpResponseRedirect('/')
        else:
            err_msg = "用户名或密码错误!"

    return render(request, 'login.html', {'err_msg': err_msg})

def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id
            new_img_path = handle_uploaded_file(request, request.FILES['head_img'])
            form_data['head_img'] = new_img_path
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request, 'new_article.html', {'new_article_obj': new_article_obj})
        else:
            print('err', form.errors)


    category_list = models.Category.objects.all()
    return render(request, 'new_article.html', {'category_list': category_list})

def add_comment(request):
    comment_form = CommentForm(request.POST)
    print(comment_form["comment"])
    if comment_form.is_valid():
        comment_data = comment_form.cleaned_data
        comment_data['user_id'] = request.user.userprofile.id
        comment_data['parent_comment_id'] = None
        new_comment_obj = models.Comment(**comment_data)
        new_comment_obj.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')
    else:
        return HttpResponse('{"status": "fail"}', content_type='application/json')


