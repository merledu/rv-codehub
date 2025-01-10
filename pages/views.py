from django.shortcuts import render
from questions.models import QuestionGroup
from django.contrib.auth.decorators import login_required
from .models import BugReport
from icecream import ic

def home_view(request):
    question_groups = QuestionGroup.objects.all()
    user = request.user
    print(user)
    context = {
        'question_groups': question_groups,
        'user': user
    }
    return render(request, 'home.html', context)

@login_required
def bug_report(request):
    if request.method == 'POST':
        name = request.user.username
        email = request.user.email
        bug_description = request.POST.get('bug')
        steps_to_reproduce = request.POST.get('steps')
        severity = request.POST.get('severity')

        ic(name)
        ic(email)
        ic(bug_description)
        ic(steps_to_reproduce)
        ic(severity)

        BugReport.objects.create(
            name=name,
            email=email,
            bug_description=bug_description,
            steps_to_reproduce=steps_to_reproduce,
            severity=severity
        )
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'bug_report.html', context)