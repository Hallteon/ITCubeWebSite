from django.views.generic import ListView, DetailView, CreateView

from articles.forms import AddArticleForm
from articles.models import Article
from utils.utils import DataMixin


class AddArticle(DataMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'articles/add_article.html'
    success_url = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание статьи')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.username = self.request.user.username

        instance.save()

        return super().form_valid(form)


class ShowArticles(DataMixin, ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Статьи')
        context['cat_selected'] = 0

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ShowArticle(DataMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['article'])

        return dict(list(context.items()) + list(c_def.items()))
