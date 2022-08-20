from articles.models import Category

title = ' | IT-Hogwarts'


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        context['title'] = context['title'] + title
        categories = Category.objects.all()
        context['categories'] = categories

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context