from django import forms
import os
from .models import Comment

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=1)
    summary = forms.CharField(max_length=255, min_length=1)
    head_img = forms.ImageField()
    category_id = forms.IntegerField()
    content = forms.CharField(min_length=10)

def handle_uploaded_file(request, f):
    base_img_upload_path = 'statics/imgs'
    user_path = '%s/%s' %(base_img_upload_path, request.user.userprofile.id)

    if not os.path.exists(user_path):
        os.makedirs(user_path)
    with open("%s/%s" %(user_path, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/static/imgs/%s/%s" %(request.user.userprofile.id, f.name)

class CommentForm(forms.Form):
    article_id = forms.IntegerField()
    comment = forms.CharField(min_length=2)
