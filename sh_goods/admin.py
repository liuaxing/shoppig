from django.contrib import admin
from sh_goods.models import GoodInfo, TypeInfo,GoodImage
# Register your models here.
admin.site.register(GoodInfo)
admin.site.register(TypeInfo)
admin.site.register(GoodImage)
