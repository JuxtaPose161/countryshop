from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Country
import json
with open('D:\PyCharm\PyProject1\something\db-country.json') as f:
    data = json.load(f)

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
