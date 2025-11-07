from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import NewsForm, SearchForm
from .models import *


def index(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        news = News.objects.all()
        cat = Category.objects.all()
        if form.is_valid():
            query = form.cleaned_data.get("title")
            name = news.filter(title__icontains = query)
    return render(request, "index.html", {"news": news, "cat": cat, "form": form})

def category(request, pk):
    news = News.objects.filter(category=pk)
    category = Category.objects.all()
    context = {
        "news": news,
        "category": category,
        "title": "NEWS TITLE"
    }


    return render(request, 'category.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})


def detail_new(request, pk):
    new = get_object_or_404(News, id=pk)
    context = {
        "new": new
    }
    return render(request, 'detail_new.html', context=context)



def update_new(request, pk):
    new = get_object_or_404(News, id=pk)
    # new = News.objects.get(pk=new_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm(instance=new)
    return render(request, 'update_new.html', {'form': form, 'new': new})



def del_new(request, pk):
    new = get_object_or_404(News, id=pk)
    new.delete()
    news = News.objects.all()
    category = Category.objects.all()
    context = {
        "news": news,
        "category": category,
        "title": "NEWS TITLE"
    }
    return render(request, 'index.html', context=context)



class HomeNews(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NEWS TITLE'
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(is_bool=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['pk'])


class ViewNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'index.html'
    pk_url_kwarg = 'pk'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'add_news.html'
    success_url = reverse_lazy('home')


class NewsUpdate(UpdateView):
    form_class = NewsForm
    template_name = "update_new.html"
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'
