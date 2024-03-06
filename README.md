# 命令

## 获取支持的命令

```powershell
python manage.py
```

## 启动项目

```powershell
python manage.py runserver [ip:][port]

#当 ip = 0.0.0.0 时，允许局域网内访问
```

## 新建应用

```powershell
python manage.py startapp [AppName]
```

## 创建管理员账号

```powershell
python manage.py createsuperuser
# 输入账户，邮箱，密码后，完成！

# ----启动项目后------
# http://127.0.0.1:8000/admin/ 进入管理员登录界面 
```

## 数据库表模板及运用

```powershell
# 给 polls 创建 生成数据库的脚本（0001_initial.py）
python manage.py makemigrations polls

# 展示 polls 脚本要执行的sql语句（展示内容跟使用的数据库有关）
python manage.py sqlmigrate polls 0001

# 运行脚本生成数据库表结构
python manage.py migrate

# 进入项目的 命令行
python manage.py shell

# 操作数据库表的一些用法
# https://docs.djangoproject.com/zh-hans/5.0/intro/tutorial02/
```
