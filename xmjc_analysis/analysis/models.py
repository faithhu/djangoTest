from django.db import models

class User(models.Model):
	username = models.CharField('用户名', max_length=30)
	userpass = models.CharField('密码', max_length=30)
	useremail = models.CharField('邮箱', max_length=30)
	usertype = models.CharField('用户类型', max_length=30)

	def __str__(self):
		return self.username