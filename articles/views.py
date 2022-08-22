from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from articles.forms import AddArticleForm
from articles.models import Article, Category
from utils.utils import DataMixin


class AddArticle(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'articles/add_article.html'
    success_url = reverse_lazy('articles')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание статьи')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.username = self.request.user
        obj.save()

        return super().form_valid(form)


class ShowArticles(DataMixin, ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Статьи')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('-create_time')


class ShowArticle(DataMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['article']))

        return dict(list(context.items()) + list(c_def.items()))


class ShowCategory(DataMixin, ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True).order_by('-create_time').select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_cat = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title=str(selected_cat.name), selected_cat=selected_cat.pk)

        return dict(list(context.items()) + list(c_def.items()))

