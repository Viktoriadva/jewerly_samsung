from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Article
def index(request):
    latest_products_l = Article.objects.order_by('-pub_date')[:6]
    return render(request,'articles/list_jew.html',{'latest_products_l':latest_products_l})

def detail(request,article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Продукт не найден!")
    latest_comments_l = a.comment_set.order_by('-id')[:10]
    return render(request,'articles/detail.html', {'article': a, 'latest_comments_l': latest_comments_l})


def leave_comment(request,article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Продукт не найден!")
    a.comment_set.create(author_name= request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('articles:detail', args = (a.id)))