from django.db import models
from core.models import Languages
# Create your models here.
class QuestionGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100, default='Untitled Question')
    question = models.TextField()
    question_group = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1)
    test_case = models.TextField(blank=True, null=True)
    answer_template = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

        # python3 manage.py shell -c "import json; from questions.models import Question; print(json.dumps(list(Question.objects.values())))"

class Submission(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    test_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.question.title}"