from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Country, FlagColors

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
