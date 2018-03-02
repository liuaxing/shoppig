from sh_goods.views import *
from django.urls import path, re_path
urlpatterns = [
     re_path('^list_(\d+)_(\d+)_(\d+)$', typelist),
     re_path('^(\d+)$',detail),
     path('', index, name='index'),
]
