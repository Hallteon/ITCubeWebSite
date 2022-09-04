from articles.models import Category, Tag


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        context['title'] = context['title']

        categories = Category.objects.all()
        context['categories'] = categories

        if 'selected_cat' not in context:
            context['selected_cat'] = 0

        if 'selected_tag' not in context:
            context['selected_tag'] = 0

        return context