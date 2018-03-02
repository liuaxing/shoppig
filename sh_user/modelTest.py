from sh_user.models import Address
# 查询
adds1=Address.objects.all()# 查询   获取所有地址
add=Address.objects.get(id=1,reciver='lisi')  #获取指定字段的记录  可以加多个条件
adds2=Address.objects.all().values_list('id','reciver')#过滤字段
add2=Address.objects.filter(uid=1,reciver='lisi').all() #符合过滤的所有记录
add3=Address.objects.filter(uid=1,reciver='lisi').first()#符合过滤的第一条记录

#新增
Address.objects.create(reciver='zhangsan',sheng='heilongjiang') #新增一条数据
add4=Address()
add4.reciver='wangwu'
add4.save()

#删除
Address.objects.filter(uid=1,reciver='lisi').delete() #删除指定数据

#更新
Address.objects.filter(uid=1,reciver='lisi').update(reciver='zhaoliu',sheng='shenyang') #更新指定数据


