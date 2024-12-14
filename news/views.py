from django.shortcuts import render, redirect
from .models import News, Category
from django.shortcuts import render, get_object_or_404


def main(request):
    news = News.objects.filter(is_publish=True).order_by('-created_at')
    category = Category.objects.all()

    return render(request, 'index.html', {'news':news, 'category':category})


def categorys(request, id):
    category = get_object_or_404(Category, id=id)
    news = News.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'category.html', {'category':category, 'news':news, 'categories': categories})

def detal_news(request, id):



    return render(request, 'detal_news.html', )

