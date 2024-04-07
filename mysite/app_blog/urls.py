# app_blog/urls.py

from django.urls import path
from .views import ArticleCategoryList

urlpatterns = [
    # ... інші маршрути ...
    path('articles/category/<slug:slug>/', ArticleCategoryList.as_view(), name='articles-category-list'),
]
