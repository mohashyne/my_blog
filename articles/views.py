from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
# from django.http import HttpResponse

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

# for testing
# def article_details(request, slug):
#     return HttpResponse(slug)


def article_details(request, slug):
    return render(request, 'articles/article_details.html')



