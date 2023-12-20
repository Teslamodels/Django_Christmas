from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

class ArticleHome(ListView):
    model = Article
    template_name = 'ArticleHome.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'ArticleDetail.html'

class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'ArticleUpdate.html'
    fields = ['Title', 'Summary', 'Body', 'Photo', 'Author']

class ArticleDelete(DeleteView):
    model = Article
    template_name = 'ArticleDelete.html'
    success_url = reverse_lazy('article')

class ArticleCreate(CreateView):
    model = Article
    template_name = 'ArticleCreate.html'
    fields = ['Title', 'Summary', 'Body', 'Photo', 'Author']