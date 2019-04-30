
from django.urls import path

from . import views

from .views import QuestionView
from .views import ChoiceView

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('new_question/', views.new_question, name='new_question'),
    path('save_question/', views.save_question, name='save_question'),
    path('sign_up/', views.new_user, name='new_user'), # GET
    path('save_user/', views.new_user, name='save_user'), # POST
    path('questions/', QuestionView.as_view()),
    path('questions/<int:question_id>/choices/', ChoiceView.as_view()),
]
