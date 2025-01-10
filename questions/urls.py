from django.urls import path
from .views import *

app_name = 'questions'

urlpatterns = [
    path('group/<int:group_id>/', questions_groups , name='q_group'),
    path('<int:question_id>/', question, name='question'),
    path('report/<int:group_id>/', generate_report, name='generate_report'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]