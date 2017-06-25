# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#新增元祖用于设置消息类型枚举项
KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文体资讯', '文体资讯'),
    ('个人心情', '个人心情'),
    ('其他', '其他'),
)

class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=200, default='匿名')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES,default=KIND_CHOICES[0])

class Register(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

# Create your models here.
