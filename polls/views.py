from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# 展示所有问题
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # 把读取到的数据返回页面
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 使用内置的render方法，返回数据
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# 展示投票界面
def detail(request, question_id):
    # 判断是否存在该 id，不存在 则展示404路径页面（Http404），存在 则展示对应id的投票结果
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     # raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})

    # 使用你内置函数get_object_or_404实现上述功能
    # 相似功能的函数还包含 get_list_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# 展示投票成功页面
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    response = "You're looking at the results of question <br>%s-\"%s\"."
    return HttpResponse(response % ( question.id, question.question_text, ))

# 用于投票的接口
# 报错返回 提示信息到投票界面
# 成功的话展示成功页面
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

