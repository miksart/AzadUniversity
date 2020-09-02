from django.urls import path

from Core.views import ArticleDetailView, ArticleListView, homepage, contact_view

urlpatterns = [
    path('contact-us/', contact_view, name="contact"),
    path('articles/', ArticleListView.as_view(), name="articles"),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name="article_detail_view"),
    path('', homepage, name="homepage")
]
