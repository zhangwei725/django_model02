from django.db import models


# ctrl + shift  + u   大小写转化
class User(models.Model):
    user_id = models.AutoField('用户ID', primary_key=True)
    username = models.CharField('用户名', max_length=64, unique=True)
    real_name = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=100, null=True)
    telno = models.CharField(max_length=11, null=True)
    mobile = models.CharField(max_length=11, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=64, null=True)
    state = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)

    class Meta:
        db_table = 't_user'
