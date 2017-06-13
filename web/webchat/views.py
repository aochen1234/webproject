from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import Column, Comment, Article, UserProfile, WebGroup
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from .scripts import verify_code
from web import settings
import os
import random
import datetime
import json
import markdown2
import string


# Create your views here.

columns = Column.objects.all()
articles = Article.objects.all()


def index(request):
    cus_list = Article.objects.all()
    paginator = Paginator(cus_list, 1)

    page = request.GET.get('page')
    if page:
        article_list = paginator.page(page).object_list
    else:
        article_list = paginator.page(1).object_list
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'cus_list': customer, 'columns': columns, 'articles': article_list})


def column_page(request, column_id):
    column_list = get_object_or_404(Column, id=column_id)
    article_list = column_list.article_set.all()

    return render(request, 'column.html', {'columns': columns, 'article_list': article_list})


def article_page(request, article_id):
    article_list = get_object_or_404(Article, id=article_id)
    content = markdown2.markdown(article_list.status, extras=["code-friendly",
        "fenced-code-blocks", "header-ids", "toc", "metadata"])
    return render(request, 'article.html', {'columns': columns, 'article_list': article_list,
                        'content': content})


@csrf_exempt
def comment(request, article_id):
    if request.method == 'POST':
        comments = request.POST['comment']
        if len(comments) < 5:
            result = u'评论数需大于5'
            return HttpResponse(json.dumps({'result': result}))
        else:
            result = 'successfully'
            Comment.objects.create(content= comments, article_id=article_id)
            return HttpResponse(json.dumps({'result': result}))


def get_comment(request, article_id):
    article_list = get_object_or_404(Article, id=article_id)
    comments = article_list.comment_set.all()
    html = ''
    for i in comments:
        ele = '<div class="row"><article class="col-xs-12"><p class="pull-right"><span class="label label-default">作者:' + 'i.user' + '</span></p><p>' + i.content + '<ul class="list-inline"><li><a href="#"></a></li></ul></article></div><hr>'
        html += ele
    return HttpResponse(json.dumps({'answer': html}))


def webchat(request):
    username = UserProfile.objects.all()
    webname = WebGroup.objects.all()
    return render(request, 'webchat.html', {'username': username, 'webname': webname})


def test(request):
    return render(request, 'test.html')


def acc_login(request):
    today_str = datetime.date.today().strftime("%Y%m%d")
    verify_code_img_path = "%s/%s" %(settings.VERIFICATION_CODE_IMGS_DIR, today_str)
    if not os.path.isdir(verify_code_img_path):
        os.makedirs(verify_code_img_path,exist_ok=True)
    print("session:", request.session.session_key)
    random_filename = "".join(random.sample(string.ascii_lowercase,4))
    random_code = verify_code.gene_code(verify_code_img_path,random_filename)
    cache.set('my_code', random_code,30)
    return render(request, 'login.html', {"filename": random_filename, "today_str": today_str})


def checkcode(request):
    err_msg = ''
    if request.method == "POST":
        _verify_code = request.POST.get('verify_code')
        if cache.get('my_code') == _verify_code:
            err_msg = 'successful'
        else:
            err_msg = "error!"

    return render(request, 'test.html', {'error': err_msg})
