from django.shortcuts import render, get_object_or_404
from . import models
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic


class CharDetailView(generic.DetailView):
    template_name = 'chars/chars_detail.html'
    context_object_name = 'char_id'
    pk_url_kwarg = 'id'
    model = models.CharsErha
    
    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_blog = request.session.get('viewed_blog', [])
        
        if obj.pk not in views_blog:
            self.model.objects.filter(pk=obj.pk).update(views=F('views')+1)
            views_blog.append(obj.pk)
            request.session['viewed_blog'] = views_blog
            obj.refresh_from_db()
        return obj 



class SearchView(generic.ListView):
    template_name = 'chars/chars_detail.html'
    model = models.CharsErha
    context_object_name = 'char'
    
    def get_queryset(self):
        return self.model.objects.filter(name__icontains=self.request.GET.get('s'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context 


class CharErhaView(generic.ListView):
    template_name = 'chars/chars_list.html'
    model = models.CharsErha
    paginate_by = 2
    ordering = ['-id']
    context_object_name = 'chars'
    
    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part'] = context['page_obj']
        return context


class CharErha(generic.TemplateView):
    template_name = 'char1.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Erha's characters"
        context['chars'] = [
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
                }
        ]
        return context


class Info(generic.TemplateView):
    template_name = 'me1.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'full_name': "Kirkeeva Amina",
            'age': 18,
            'nationality': 'kyrgyz, uighur',
            'height': '175',
            'hobby': ['reading', 'drawing', 'academics', 'gaming']
        })
        return context 
