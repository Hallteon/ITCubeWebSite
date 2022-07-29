title = 'IT-Hogwarts | '

class DataMixin():
    def get_user_context(self, **kwargs):
        context = kwargs

        context['title'] = title + context['title']

        return context