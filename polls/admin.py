from django.contrib import admin

# Register your models here.

# 向管理页面中加入投票应用
# 用于 管理员或用户，修改该表
from .models import Question

admin.site.register(Question)