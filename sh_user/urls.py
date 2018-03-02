
from django.urls import path,include
from sh_user.views import *

urlpatterns = [
     path('login',login),
     path('register',register),
     path('reg',register_handle),
     path('log_hand',login_handle),
     path('logout',logout),
     path('checkname',register_exist),
     path('userinfo',user__center_info),
     path('userupdate',userupdate),
     path('shdz',shdz),
     path('add_save',add_save),
     path('mrdz',mrdz),
     path('scdz',scdz),
     path('xgdz',xgdz)
]
