from django.urls import path
from . import views
from .views import Userviews,DetailUser,Userviews2


urlpatterns = [
    path('', views.start, name='start'),
    path('start/', views.main, name='main'),
    path('members2/', views.members2, name='members2'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('members/delete/<slug:slug>', views.delete_member, name='delete_member'),
    path('members/update/<slug:slug>', views.update_member, name='update_member'),
    path('members/update_form/<slug:slug>', views.form_update_member, name='form_update_member'),
    path('members/create_member/', views.create_member, name='create_member'),
    path('user/user_list/', Userviews.as_view(),name='Userviews'),
    path('user/user_list2/', Userviews2.as_view(), name='Userviews2'),
    path('user/detail_user_list/<int:pk>', DetailUser.as_view()),
    path('user/delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('user/create_user/', views.create_user, name='create_user'),
    path('user/edit_user/<int:id>', views.edit_user, name='edit_user'),# url para formulario update
    path('user/update_user/', views.update_user, name='update_user'),

]

'''
path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''