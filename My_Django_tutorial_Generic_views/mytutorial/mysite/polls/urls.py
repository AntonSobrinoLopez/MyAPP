from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('polls1/', views.index_1, name='index_1'),
    path('polls2/', views.index_2, name='index_2'),
    path('polls3/', views.index_3, name='index_3'),
    path('polls4/', views.detail_1, name='detail_1'),
    path('polls5/', views.results_1, name='results_1'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]