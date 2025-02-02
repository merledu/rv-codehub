from django.contrib import admin
from .models import QuestionGroup, Question, Submission, Contest
# Register your models here.

admin.site.register(QuestionGroup)
admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(Contest)
