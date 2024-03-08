from django.urls import path

from . import views

# 命名空间
# 用于模板中获取准确路由：polls\templates\polls\index.html
app_name = "polls"

urlpatterns = [
    # 视图逻辑自定义
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),


    # 通用视图模式
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]