from django.db import models
from sh_user.models import User
from sh_goods.models import GoodInfo
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey('sh_user.User',None)
    goods=models.ForeignKey('sh_goods.GoodInfo',None)
    count=models.IntegerField(default=0)
