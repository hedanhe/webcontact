from django.db import models
from web import models as bbs_models

class QQGroup(models.Model):
    name = models.CharField(max_length=64)
    founder = models.ForeignKey(bbs_models.UserProfile, on_delete=models.CASCADE)     #创始人
    brief = models.TextField(max_length=1024)           #群介绍
    admin = models.ManyToManyField(bbs_models.UserProfile, related_name='group_admin')
    members = models.ManyToManyField(bbs_models.UserProfile, related_name='group_member')
    member_limit = models.IntegerField(default=200)     #群成员数量

    def __unicode__(self):
        return self.name