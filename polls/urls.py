
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/message/', views.message, name='message'),
    path('new_question/', views.new_question, name='new_question'),
    path('save_question/', views.save_question, name='save_question'),
    path('new_user/', views.new_user, name='new_user'),
    path('save_user/', views.save_user, name='save_user'),
    path("This-is-json/", views.this_is_json, name="winnie_poo"),
]
