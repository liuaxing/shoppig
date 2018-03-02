from django.db import models

# Create your models here.
class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    pid=models.IntegerField(default=0)
    scbz=models.BooleanField(default=False)#使用逻辑删除
    level=models.IntegerField(default=1)
    turl=models.CharField(max_length=64,default='')

    def __str__(self):       #这里是在admin显示的内容
        return self.ttitle


class GoodInfo(models.Model):
    gtitle=models.CharField(max_length=50)
    gpic=models.ImageField(upload_to='sh_goods')
    gprice=models.DecimalField(max_digits=8,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(max_length=20,default='')
    gclick=models.IntegerField()
    gintro=models.CharField(max_length=200)
    # gdetial=HTMLField()
    gtype=models.ForeignKey('TypeInfo',None)
    gkucun=models.IntegerField(default=0)
    gadv=models.BooleanField(default=False)
    def __str__(self):
        return self.gtitle

class GoodImage(models.Model):
    gid=models.ForeignKey('GoodInfo',None)
    lbsm=models.CharField(max_length=20,default='')
    gpic = models.ImageField(upload_to='sh_goods')
    def __str__(self):
        return self.lbsm

