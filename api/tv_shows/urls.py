from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tv_shows import views

urlpatterns = [
    path('shows/', views.ShowList.as_view()),
    path('categories/', views.ShowListByCategory.as_view()),
    path('link/', views.ShowLinkByCategory.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)