# app_blog/views.py

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Можливо деякий контекст
        return context

# app_blog/views.py

from django.views.generic import ListView
from .models import Category

class ArticleCategoryList(ListView):
    model = Category
    template_name = 'articles_category_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Category.objects.filter(category__slug=self.kwargs.get('slug'))
