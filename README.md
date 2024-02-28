# mySite

## 命令

### 获取支持的命令

```powershell
python manage.py
```

### 启动项目

```powershell
python manage.py runserver [ip:][port]

#当 ip = 0.0.0.0 时，允许局域网内访问
```

### 新建应用

```powershell
python manage.py startapp [AppName]
```

### 创建管理员账号

```powershell
python manage.py createsuperuser
# 输入账户，邮箱，密码后，完成！

# ----启动项目后------
# http://127.0.0.1:8000/admin/ 进入管理员登录界面 
```

