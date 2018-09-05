from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse

# M
# V
# 程序员 入门

#  第一步  用户输入登录界面的的网站
#  第二歩   服务器返回登录界面
#  第三步   用户输入用户名密码
#  第四歩  提交到服务器
#  第五步 服务器获取用户输入的数据
#  第六步 从数据库查询数据 根据数据判断是否登录成功 如果错误提示相应错误的信息
#
from account.models import User


def login_view(request):
    return render(request, 'login.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 返回列表
    users = User.objects.filter(username=username)
    if users:
        user = users.first()
        if users.first().password == password:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('您输入的密码错误')
    else:
        return HttpResponse('用户名不存在')


# 保存对象
# 1> 创建对象
# 2> 掉用模型的save()方法
def insert(request):
    # save()
    user = User(username='1111', password='123456')
    # user.username = '111'
    # force_insert   强行添加  开发中不要使用 因为可能会违反约束,导致脏数据
    #  force_update  强制更新
    user.save()
    return HttpResponse('添加单个对象')


def create(request):
    # save()
    User.objects.create(username='1111', password='111111')
    # user.username = '111'
    # force_insert   强行添加  开发中不要使用 因为可能会违反约束,导致脏数据
    #  force_update  强制更新

    return HttpResponse('添加单个对象')


def bulk_create(reuqest):
    # 批量添加  推荐使用
    users = []
    for i in range(100):
        users.append(User(username='test%s' % i, password='123456'))
    User.objects.bulk_create(users)

    # for i in range(101, 201):
    #     user = User(username='test%s' % i, password='123456')
    #     user.save()
    return HttpResponse('批量添加对象')


# QuerySet对象的方法
# 第一步 该条记录一定要存在 根据条件查询出该记录
#
#
def update(request):
    """
    #  ------ 第一种方式
    # 1.查询出该条记录
    user = User.objects.get(user_id=1)
    # 2. 修改数据
    user.username = '空空'
    user.password = '123'
    user.price += 100.00
    # 3.更新
    user.save(update_fields=['username', 'password'])
    """
    # 第二种方式
    # UPDATE  TABLE  SET  STATE=0
    # User.objects.filter(user_id=1).update(state=1)

    # F() 配合使用
    # 购物车   数量 + 1
    User.objects.update(price=F('price') + 2.00)

    return HttpResponse('通过save方法更新')


# 1>查询对象
def delete(request):
    user = User.objects.get(user_id=1)
    user.delete()
    return HttpResponse('通过save方法更新')


# 补充部分 限定符     and  or  not
#  in   like   between   and

# 限定符   相当于  where 后面的限定符
# 双下划线    属性名__限定符
def ext(request):
    # 比较运算符  gt 大于   gte大于等于
    # select * from  user  where  user_id >= 10
    # users = User.objects.filter(user_id=10)
    # for user in users:
    #     print(user.user_id)

    #   包含  in  lik---->contain    between and ---->  range  null-->isnull

    #   in的操作
    # users =  User.objects.filter(user_id__in=[1, 2, 3])

    # like '%gtest%'  的操作
    # username__icontains  忽略大小写
    #   startswith   istartswith  endswith  iendswith
    # users = User.objects.filter(username__contains='test')
    # users = User.objects.filter(username__icontains='test')
    # for user in users:
    #     print(user.username)

    # between  and

    users = User.objects.filter(user_id__range=[3, 10])
    for user in users:
        print(user.user_id)

    return HttpResponse('限定符的使用')
