from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

from .models import Country, FlagColors, Article, User, Cart
from .form import ArticleForm


def score_sorted_main_page(request, level):
    if request.method == 'GET':
        search_get = request.GET.get('search', '')
        if level == 'A':
            obj = Country.objects.filter(gnp__gt=372881454000).filter(name__istartswith=search_get)
        elif level == 'B':
            obj = Country.objects.filter(gnp__range=(65736565999, 372881454000)).filter(name__istartswith=search_get)
        elif level == 'c':
            obj = Country.objects.filter(gnp__range=(18627850000, 65736565999)).filter(name__istartswith=search_get)
        elif level == 'D':
            obj = Country.objects.filter(gnp__range=(4598796000, 18627850000)).filter(name__istartswith=search_get)
        elif level == 'E':
            obj = Country.objects.filter(gnp__lt=4598796000).filter(name__istartswith=search_get)
        else:
            return redirect('shop')


        page_num = request.GET.get('page', 1)
        paginator = Paginator(obj, 6)
        page_obj = paginator.get_page(page_num)
        return render(request, 'mainshop/main.html', {'obj': page_obj, 'search': search_get})

def color_sorted_main_page(request, color):
    search_get = request.GET.get('search', '')
    page_num = request.GET.get('page', 1)
    tag = FlagColors.objects.get(name=color)
    obj = tag.colors.all().filter(name__istartswith=search_get)

    paginator = Paginator(obj, 6)
    page_obj = paginator.get_page(page_num)
    return render(request, 'mainshop/main.html', {'obj': page_obj, 'search': search_get})

def country_article_page(request, country):
    obj = Country.objects.get(slug=country)
    author_name = request.GET.get('author', None)
    if request.user.is_authenticated:
        is_write_article = request.user.article.filter(country=obj).exists()
    else:
        is_write_article = False
    if author_name:
        author = User.objects.get(username=author_name)
        article = obj.about.get(owner=author)
    else:
        article = obj.about.first()
    return render(request, 'mainshop/country.html', {'article': article, 'obj': obj, 'is_write_article': is_write_article})

def put_in_cart(request, country):
    user_cart = Cart.objects.get(owner=request.user)
    obj = Country.objects.get(slug=country)
    if user_cart.purchases.filter(pk=obj.pk).exists():
        user_cart.purchases.remove(obj)
        print("Удалено")
    else:
        user_cart.purchases.add(obj)
        print("Добавлено")

    previous_url = request.META.get('HTTP_REFERER')
    return redirect(previous_url)

def user_cart_page(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.get(owner=request.user)
        obj = user_cart.purchases.all()
        if not obj.exists():
            return render(request, 'mainshop/cart.html', {'obj': obj, 'sum': 0})
        sum = user_cart.purchases.aggregate(Sum('price'))
        clean_sum = round(sum['price__sum'], 2)
        return render(request, 'mainshop/cart.html', {'obj': obj, 'sum': clean_sum})
    return redirect('shop')
def create_article(request, country):
    if request.method == 'POST':
        print(request.POST)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.country = Country.objects.get(slug=country)
            article.save()
            return redirect('shop_article', country=country)
    else:
        form = ArticleForm()
    return render(request, 'mainshop/article_form.html', {'form': form})
def update_article(request, country):
    obj = Country.objects.get(slug=country)
    article = get_object_or_404(Article, owner=request.user, country=obj)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('shop_article', country=country)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'mainshop/article_form.html', {'form': form})

def delete_article(request, country):
    obj = Country.objects.get(slug=country)
    article = get_object_or_404(Article, owner=request.user, country=obj).delete()
    return redirect('shop_article', country=country)
def to_need_page(request):
    return redirect('shop', permanent=True)
def main_page(request):
    if request.method == 'GET':
        search_get = request.GET.get('search', '')
        page_num = request.GET.get('page', 1)
        obj = Country.objects.filter(name__istartswith=search_get)

        paginator = Paginator(obj, 6)
        page_obj = paginator.get_page(page_num)
        return render(request, 'mainshop/main.html', {'obj': page_obj, 'search': search_get})
# Create your views here.
