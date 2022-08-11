from django.views.generic import ListView, DetailView

from articles.models import Article
from utils.utils import DataMixin


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
