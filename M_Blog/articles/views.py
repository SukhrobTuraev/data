from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('type_new', 'title', 'summary', 'body', 'photo')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

def SportView(request):
    data = Article.objects.filter(type_new  =  "Sport")
    return render(request, 'sport.html', {'data': data})

def JahonView(request):
    data = Article.objects.filter(type_new  =  "Jahon")
    return render(request, 'jahon.html', {'data': data})
def Fan_texnika(request):
    data = Article.objects.filter(type_new="Fan_texnika")
    return render(request, 'fan_texnika.html', {'data': data})

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin,  CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('type_new', 'title', 'summary', 'body', 'photo')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


def info(request):
    return render(request, 'homepage.html')
