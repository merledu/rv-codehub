from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'),
    path('bug_report/', bug_report, name='bug_report'),
]
