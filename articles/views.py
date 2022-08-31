from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from articles.forms import AddArticleForm, AddCommentForm
from articles.models import Article, Category
from users.models import Ip
from utils.utils import DataMixin


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


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
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.article = self.get_object()
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        ip = get_client_ip(self.request)

        if Ip.objects.filter(ip=ip).exists():
            self.get_object().views_count.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(user=self.request.user, ip=ip)
            self.get_object().views_count.add(Ip.objects.get(ip=ip))

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

