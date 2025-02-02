from django.urls import path
from .views import *

app_name = 'questions'

urlpatterns = [
    path('group/<int:group_id>/', questions_groups , name='q_group'),
    path('<int:question_id>/', question, name='question'),
    path('report/<int:group_id>/', generate_report, name='generate_report'),
    path('contest/<int:group_id>/', add_user_to_contest, name='add_user_to_contest'),
    path('contest/deduct/<int:contest_id>/<int:time>/', deduct_time, name='deduct_time'),
    path('contest/increase/<int:contest_id>/<int:time>/', increase_time, name='increase_time'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]