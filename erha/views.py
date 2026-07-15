from django.shortcuts import render, get_object_or_404
from . import models
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import F


def char_detail_view(request, id):
    if request.method == 'GET':
        char_id = get_object_or_404(models.CharsErha, id=id)

        views_blog = request.session.get('viewed_blog', [])

        if id not in views_blog:
            char_id.views = F("views")+1
            char_id.save()
            char_id.refresh_from_db()
        views_blog.append(id)
        request.session['viewed_blog'] = views_blog


    return render(request, 'chars/chars_detail.html', {'char_id': char_id})



def search_view(request):
    query = request.GET.get('s', '')
    if query:
        character = models.CharsErha.objects.filter(name__icontains=query)
        if not character.exists():
            return HttpResponse('No such name here')
    else:
        return HttpResponse('No such name here')


def char_detail_view(request, id):
    if request.method == 'GET':
        char_id = get_object_or_404(models.CharsErha, id=id)
    return render(request, 'chars/chars_detail.html', {'char_id':char_id})


def char_erha_view(request):
    if request.method == 'GET':
        chars = models.CharsErha.objects.all().order_by('-id')
        novel = models.Fragments.objects.all().order_by('-id')

        paginator = Paginator(chars, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

    return render(request, 'chars/chars_list.html',
        {
            'chars': page_obj,
            'part': page_obj,
            'novel': novel,
        }
    )



def char_erha(request):
    if request.method == 'GET':
        chars = {
            'title': "Erha's characters",
            'characters':[
                {
            'name':"Chu Wanning",
            'age': 32,
            'element': ["Metal", "Wood"],
            'weapon': ["Tianwen", "Jiuge", "Huaisha"],
            'organization': "Sisheng Peak"
                },
                {
            'name':"Mo Ran",
            'age': 37,
            'element': ["Fire", "Wood"],
            'weapon': ["Jiangui", "Bugui"],
            'organization': "Sisheng Peak"
                },
            ]
        }
    return render(request, 'char1.html', chars )

def info(request):
    if request.method == "GET":
            me1 = {
            'full_name': "Kirkeeva Amina",
            'age': 18,
            'nationality': 'kyrgyz, uighur',
            'height': '175',
            'hobby': ['reading', 'drawing', 'academics', 'gaming']
        }
    return render(request, 'me1.html', me1)