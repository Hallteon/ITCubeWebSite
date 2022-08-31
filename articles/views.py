from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from articles.forms import AddArticleForm, AddCommentForm
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

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        else:
            return self.form_invalid(form)

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


class ShowArticle(FormMixin, DataMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'article_id': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.article = self.get_object()
        obj.save()

        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user not in self.get_object().views_count.all():
            self.get_object().views_count.add(self.request.user)

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['article']))

        return dict(list(context.items()) + list(c_def.items()))


class ShowCategory(DataMixin, ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    allow_empty = True

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True).order_by('-create_time').select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_cat = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title=str(selected_cat.name), selected_cat=selected_cat.pk)

        return dict(list(context.items()) + list(c_def.items()))

